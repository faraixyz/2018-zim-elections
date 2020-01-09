from pathlib import Path
import re
from bs4 import BeautifulSoup
from elect_parser import ElectParser


def remove_extra_tags(soup):
    """
    Removes the headers, footer and endOfContent marker in each page
    :param soup: A beautiful soup object
    """
    footer_text = re.compile(r"\d+ of 178")
    page_footers = soup.find_all(text=footer_text)
    page_header_text = "2018 VOTER POPULATION PER POLLING STATION"
    page_headers = soup.find_all(text=page_header_text)
    page_end_markers = soup.find_all("div", {"class": "endOfContent"})

    for header, footer, marker in zip(page_headers, page_footers,
                                      page_end_markers):
        header.parent.decompose()
        footer.parent.decompose()
        marker.decompose()


class StationsParser(ElectParser):
    def __init__(self, label, src):
        with open(src, 'r', encoding="utf-8") as html_doc:
            soup = BeautifulSoup(html_doc, 'html.parser')
        remove_extra_tags(soup)
        pages = soup.find_all("div", {"class": "textLayer"})
        self._fieldnames = ['ser', 'province', 'district', 'constituency',
                            'local_authority', 'ward', 'polling_station_name',
                            'polling_station_code', 'female', 'male', 'total']
        self._elects = []
        self._label = label
        for page_num, page in enumerate(pages):
            page_list = list(page)
            start = 11
            for i in range(start, len(page_list), 11):
                station = {field: '' for field in self._fieldnames}
                station['ser'] = int(page_list[i].string)
                station['province'] = page_list[i+1].string
                station['district'] = page_list[i+2].string
                station['constituency'] = page_list[i+3].string
                station['local_authority'] = page_list[i+4].string
                station['ward'] = int(page_list[i+5].string)
                station['polling_station_name'] = page_list[i+6].string
                station['polling_station_code'] = page_list[i+7].string
                station['female'] = int(page_list[i+8].string)
                station['male'] = int(page_list[i+9].string)
                station['total'] = int(page_list[i+10].string)
                self._elects.append(station)


if __name__ == "__main__":
    p = StationsParser(Path(__file__).stem,
                       Path('./data/polling-stations.html'))
    p.toAll(Path('./output'),
            schema_file=Path("./data/schemas/polling_stations.schema.sql"))
