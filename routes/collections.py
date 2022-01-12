import random
import re

import requests
from fastapi import HTTPException, Response, status
from utils import crop_image

from routes import config, router


@router.get(path="/collections", tags=['Collections'])
async def get_collection_list():
    return config.collections


@router.get(path="/collections/{name}/random", tags=['Collections'])
async def get_random_wallpaper_from_collection(name: str, download: bool = False, width: int = 0, height: int = 0):
    pack_response = requests.get(
        config.wallpaper_api_url + config.wallpaper_collection_path + name).text
    extracted_wlprs = re.findall(config.wallpaper_regex, pack_response)
    if len(extracted_wlprs) > 0:
        random_wlpr = random.choice(extracted_wlprs)
        wallpaper_url = config.wallpaper_api_url + \
            config.wallpaper_download_path+random_wlpr
        image_io = requests.get(wallpaper_url).content
        if width and height:
            image_io = await crop_image(image=image_io, width=width, height=height)
        headers = None
        if download:
            headers = {
                'Content-Disposition': 'attachment; filename="{filename}"'.format(filename=random_wlpr+'.png')
            }
        return Response(content=image_io, headers=headers, media_type='image/jpg')
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'collection not found')


@router.get(path="/collections/{name}", tags=['Collections'])
async def get_wallpapers_from_collection(name: str):
    pack_response = requests.get(
        config.wallpaper_api_url + config.wallpaper_collection_path + name).text
    extracted_wlprs = re.findall(config.wallpaper_regex, pack_response)
    extracted_wlprs = list(set(extracted_wlprs))
    if len(extracted_wlprs) > 0:
        return extracted_wlprs
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'no wallpaper found')
