import json
import os
import re
from types import SimpleNamespace

import requests


with open('config.json') as f:
    config = SimpleNamespace(**(json.loads(f.read())))
if not os.path.exists(config.wallpaper_collection_file_path):
    open(config.wallpaper_collection_file_path, 'w').close()

COLLECTIONS_STRINGS = []
with open(config.wallpaper_collection_file_path, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        COLLECTIONS_STRINGS.append(line)

existing_cols = len(COLLECTIONS_STRINGS)
print(f'{existing_cols} existing collections')


def scrape_from_cat():
    for cat in config.wallpaper_categories:
        r = requests.get(url=config.wallpaper_api_url +
                         config.wallpaper_categories_path+cat).text
        links = re.findall(config.wallpaper_collection_regex, r)
        for col in links:
            if not col in COLLECTIONS_STRINGS:
                COLLECTIONS_STRINGS.append(col)


def scrape_from_search(text):
    r = requests.get(url=config.wallpaper_api_url +
                     config.wallpaper_search_path+text).text
    links = re.findall(config.wallpaper_collection_regex, r)
    for col in links:
        if not col in COLLECTIONS_STRINGS:
            COLLECTIONS_STRINGS.append(col)


ask = input('Search for collections or enter "category" for automatically fetch all collections from categories\nSearch for collections: ')
if ask == "category":
    scrape_from_cat(ask)
else:
    scrape_from_search(ask)


new_cols = len(COLLECTIONS_STRINGS) - existing_cols
print(f'{new_cols} new collections found!')
if new_cols != 0:
    with open(config.wallpaper_collection_file_path, 'w') as f:
        for col in COLLECTIONS_STRINGS:
            f.write(col + '\n')

print(f'Saved ! Total {existing_cols + new_cols} collections')