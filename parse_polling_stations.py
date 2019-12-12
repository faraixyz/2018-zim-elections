import csv
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

def to_csv(data, dest="polling_stations.csv"):
    with open(dest, "w", newline="\n") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

def main():
    with open("data/polling-stations.html", "r", encoding="utf-8") as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
    remove_extra_tags(soup)
    pages = soup.find_all("div", {"class": "textLayer"})

    data = []
    for page_num, page in enumerate(pages):
        page_list = list(page)
        start = 0 if page_num == 0 else 11
        for i in range(start,len(page_list),11):
            data.append([elem.string for elem in page_list[i:i+11]])
    to_csv(data)

if __name__ == "__main__":
    main()
