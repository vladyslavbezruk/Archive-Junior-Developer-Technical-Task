import os

import requests
from bs4 import BeautifulSoup

import json_func
import process_page

web_site = "https://scrapeme.live/shop/"

items = []

cur_page = 1

end_page = False

while not end_page:

    cur_web_site = web_site + f'page/{cur_page}/'

    page_source = requests.get(cur_web_site)

    if page_source.status_code == 200:
        soup = BeautifulSoup(page_source.text, 'html.parser')

        print('Page: ' + cur_web_site)

        new_items = process_page.process_page(soup)

        count = len(new_items)

        if count == 0:
            end_page = True
        else:
            print(f'Added new {count} elements')

            items.extend(new_items)

    else:
        end_page = True

    cur_page += 1

print("Done")

result_file_path = os.path.join("result.json")

json_func.write_json(items, result_file_path)
