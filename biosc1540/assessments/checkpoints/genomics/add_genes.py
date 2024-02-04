import json
import re

import requests
from bs4 import BeautifulSoup


# Function to parse the markdown file and extract gene names
def parse_markdown(file_path):
    gene_names = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("## "):  # Identifies gene names
                gene_name = line.strip().removeprefix("## ")
                gene_names.append(gene_name)
    return gene_names


# Placeholder function to fetch additional information from NCBI or Uniprot
# This function should be implemented with actual requests to the APIs or web scraping tools
def fetch_gene_info(gene):
    ncbi_url = (
        f"https://www.ncbi.nlm.nih.gov/gene/?term={gene}+AND+Escherichia+coli[orgn]"
    )

    # Perform search for gene on NCBI
    ncbi_response = requests.get(ncbi_url, timeout=30)
    ncbi_soup = BeautifulSoup(ncbi_response.text, "html.parser")
    rows = ncbi_soup.find_all("tr")[1:]
    # We were redirected to the page, not search page
    gene_id = None
    if "Bibliography" in ncbi_soup.text:
        info = ncbi_soup.find("span", attrs={"class": "geneid"})
        gene_id = info.text.split(": ")[1].split(",")[0]
    else:
        for row in rows:
            if " K-12 " in row.text:
                gene_id = str(row).split('value="')[1].split('"')[0]
                break
    if gene_id is None:
        print(f"Gene {gene} not found on NCBI")
        return {}

    # Get data from gene page
    gene_url = f"https://www.ncbi.nlm.nih.gov/gene/{gene_id}"
    ncbi_response = requests.get(gene_url, timeout=30)
    ncbi_soup = BeautifulSoup(ncbi_response.text, "html.parser")
    info = ncbi_soup.find_all("dl")
    gene_desc = info[0].find_all("dd")[1].text

    # Fetching and parsing Uniprot page (if needed)
    uniprot_search_url = f"https://rest.uniprot.org/uniprotkb/search?compressed=false&format=tsv&query=%28{gene_id}+AND+Escherichia+coli%29&size=5"
    uniprot_response = requests.get(uniprot_search_url, timeout=30)
    uniprot_id = uniprot_response.text.split("\n")[1].split("\t")[0]
    uniprot_url = f"https://www.uniprot.org/uniprotkb/{uniprot_id}/entry"

    # Additional parsing for Uniprot information can be added here
    data = {
        "gene_id": gene_id,
        "gene_url": gene_url,
        "description": gene_desc,
        "uniprot_id": uniprot_id,
        "uniprot_url": uniprot_url,
    }
    return data


def save_json(gene_info, file_path):
    with open(file_path, "w") as f:
        json.dump(gene_info, f, indent=4)


# Main function to process the markdown file and output information
def process_genes(file_path, gene_info, json_path):
    gene_names = parse_markdown(file_path)
    gene_keys = gene_info.keys()
    for gene_name in gene_names:
        if gene_name in gene_keys:
            continue
        gene_details = fetch_gene_info(gene_name)
        if gene_details == {}:
            continue
        gene_info[gene_name] = gene_details
        if len(gene_info) % 10 == 0:
            save_json(gene_info, json_path)
    save_json(gene_info, json_path)
    return gene_info


# Example file path, replace with actual path
file_path = "/home/alex/repos/biosc1540-2024s/biosc1540/assessments/checkpoints/genomics/genes.md"
json_path = "/home/alex/repos/biosc1540-2024s/biosc1540/assessments/checkpoints/genomics/genes.json"

with open(json_path, "r", encoding="utf-8") as f:
    gene_info = json.load(f)

gene_info = process_genes(file_path, gene_info, json_path)
