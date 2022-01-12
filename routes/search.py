import re

import requests
from fastapi import HTTPException, status

from routes import config, router


@router.get(path="/search/{name}", tags=['Search'])
async def search_for_collections(name: str):
    print(config.wallpaper_api_url+config.wallpaper_search_path+name)
    pack_response = requests.get(
        config.wallpaper_api_url+config.wallpaper_search_path+name).text
    extracted_wlprs = re.findall(
        config.wallpaper_collection_regex, pack_response)
    extracted_wlprs = list(set(extracted_wlprs))
    if len(extracted_wlprs) > 0:
        return extracted_wlprs
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'bo result found')
