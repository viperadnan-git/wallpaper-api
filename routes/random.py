import random
import re

import requests
from fastapi import HTTPException, status
from fastapi.responses import Response
from utils import crop_image

from routes import config, router


@router.get(path="/random", tags=['Random Wallpapers'])
async def get_random_wallpaper(download: bool = False, width: int = 0, height: int = 0):
    if len(config.collections) > 0:
        pack = random.choice(config.collections)
        pack_response = requests.get(
            config.wallpaper_api_url+config.wallpaper_collection_path+pack).text
        extracted_wlprs = re.findall(config.wallpaper_regex, pack_response)
        random_wlpr = random.choice(extracted_wlprs)
        wallpaper_url = config.wallpaper_api_url + \
            config.wallpaper_download_path+random_wlpr
        image_io = requests.get(wallpaper_url).content
        if width and height:
            image_io = await crop_image(image=image_io, width=width, height=height)
        headers = None
        if download:
            headers = {
                'Content-Disposition': 'attachment; filename="{filename}"'.format(filename=random_wlpr+".png")
            }
        return Response(content=image_io, headers=headers, media_type='image/jpg')
    else:
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            'random wallpapers feature is disabled')
