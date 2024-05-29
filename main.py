import concurrent.futures
import os

import requests
from bs4 import BeautifulSoup

import json_func
import process_page

web_site = "https://scrapeme.live/shop/"
items = []
end_page = False


def fetch_and_process_page(cur_web_site):
    global end_page

    page_source = requests.get(cur_web_site)
    new_items = []
    if page_source.status_code == 200:
        soup = BeautifulSoup(page_source.text, 'html.parser')
        new_items = process_page.process_page(soup)
        count = len(new_items)
        if count > 0:
            print(f'Added new {count} elements from page: {cur_web_site}')
        else:
            end_page = True
    else:
        print(f"Failed to retrieve page: {cur_web_site}")
        end_page = True

    return new_items


def main():
    cur_page = 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        while not end_page:
            print(end_page)

            cur_web_site = web_site + f'page/{cur_page}/'
            future = executor.submit(fetch_and_process_page, cur_web_site)
            futures.append(future)
            cur_page += 1
            if len(futures) >= 8 or end_page:
                for future in concurrent.futures.as_completed(futures):
                    items.extend(future.result())
                futures = []
    print("Done")

    result_file_path = os.path.join("result.json")
    json_func.write_json(items, result_file_path)


if __name__ == "__main__":
    main()
