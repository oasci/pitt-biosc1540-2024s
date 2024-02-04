import json

# Example file path, replace with actual path
file_path = "/home/alex/repos/biosc1540-2024s/biosc1540/assessments/checkpoints/genomics/genes.md"
json_path = "/home/alex/repos/biosc1540-2024s/biosc1540/assessments/checkpoints/genomics/genes.json"

with open(json_path, "r", encoding="utf-8") as f:
    gene_info = json.load(f)

lines = ["# Genes\n", "\n"]
for gene_name, gene_info in gene_info.items():
    lines.append(f"## {gene_name}\n\n")
    lines.append(gene_info["description"] + "\n\n")
    lines.append(f"Gene ID: [{gene_info['gene_id']}]({gene_info['gene_url']})\n\n")
    lines.append(
        f"UniProt ID: [{gene_info['uniprot_id']}]({gene_info['uniprot_url']})\n\n"
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
