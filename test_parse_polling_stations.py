import unittest
from bs4 import BeautifulSoup
from parse_polling_stations import remove_extra_tags, parse_row

class TestParsePollingStations(unittest.TestCase):

    def test_remove_extra_tags(self):
        html = """
        <div>2018 VOTER POPULATION PER POLLING STATION</div>
        <div>1 of 178</div>
        <div class="endOfContent"></div>
        <a href="hi.com">hi</a>
        """
        soup = BeautifulSoup(html, "html.parser")
        remove_extra_tags(soup)
        remaining_soup = str(soup)
        self.assertNotIn("<div>2018 VOTER POPULATION PER POLLING STATION</div>", remaining_soup)
        self.assertNotIn("<div>1 of 178</div>", remaining_soup)
        self.assertNotIn('<div class="endOfContent"></div>', remaining_soup)
        self.assertIn('<a href="hi.com">hi</a>', remaining_soup)

    def test_parse_row(self):
        row_items = ["1", "2", "3", "4", "5"]
        html = "".join([f'<div class="textLayer">{h}</div>' for h in row_items])
        soup = BeautifulSoup(html, "html.parser")
        pages = soup.find_all("div", {"class": "textLayer"})
        headers = parse_row(pages)
        self.assertListEqual(headers, row_items)

if __name__ == "__main__":
    unittest.main()
