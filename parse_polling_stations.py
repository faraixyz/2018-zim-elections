import re
from bs4 import BeautifulSoup

def remove_extra_tags(soup):
    """
    Removes the headers, footer and endOfContent marker in each page
    :param soup: A beautiful soup object
    """

    footer_text = re.compile(r"\d+ of 178")
    page_footers = soup.find_all(text=footer_text)
    page_headers = soup.find_all(text="2018 VOTER POPULATION PER POLLING STATION")
    page_end_markers = soup.find_all("div", {"class": "endOfContent"})

    for header, footer, marker in zip(page_headers, page_footers, page_end_markers):
        header.parent.decompose()
        footer.parent.decompose()
        marker.decompose()

def parse_row(data_row):
    row = []
    for elem in data_row:
        row.append(elem.get_text())
    return row

def main():
    with open("polling-stations.html", "r", encoding="utf-8") as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
