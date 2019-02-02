import unittest
from bs4 import BeautifulSoup
from parse_polling_stations import remove_extra_tags

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

if __name__ == "__main__":
    unittest.main()
