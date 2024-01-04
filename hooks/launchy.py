import os

from bs4 import BeautifulSoup


def on_page_content(html, page, config, files):
    # Only Jupyter notebooks will have this div.
    if '<div class="jupyter-wrapper">' in html:
        colab_url = os.path.join(config["colab_base_url"], page.url)[:-1] + ".ipynb"
        colab_launch_html = f"""
        <div class="launchy-container">
            <a href="{colab_url}" target="_blank">
                <img src="/img/launchy/colab.svg" alt="Colab Image" style="height: 20px; width: 100%;" class="off-glb"/>
            </a>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        h1_tag = soup.find("h1")
        h1_tag.insert_after(BeautifulSoup(colab_launch_html, "html.parser"))
        return soup.prettify()
    return html
