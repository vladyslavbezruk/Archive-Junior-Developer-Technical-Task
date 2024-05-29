import unittest

import requests
from bs4 import BeautifulSoup

from process_page import process_page


class TestProcessPage(unittest.TestCase):

    def test_process_page(self):
        url = "https://scrapeme.live/shop/"
        page_source = requests.get(url).text
        soup = BeautifulSoup(page_source, 'html.parser')

        items = process_page(soup)

        self.assertTrue(items)

        self.assertEqual(len(items), 16)

        for item in items:
            self.assertTrue(item['id'])
            self.assertTrue(item['name'])
            self.assertTrue(item['price'])
            self.assertTrue(item['sku'])
            self.assertTrue(item['image_url'])


if __name__ == '__main__':
    unittest.main()
