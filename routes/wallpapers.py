import requests
from fastapi.responses import Response
from utils import crop_image

from routes import config, router


@router.get(path="/wallpaper/{name}", tags=['Wallpaper'])
async def get_wallpaper(name: str, download: bool = False, width: int = 0, height: int = 0):
    wallpaper_url = config.wallpaper_api_url+config.wallpaper_download_path+name
    image_io = requests.get(wallpaper_url).content
    if width and height:
        image_io = await crop_image(image=image_io, width=width, height=height)
    headers = None
    if download:
        headers = {
            'Content-Disposition': 'attachment; filename="{filename}"'.format(filename=name+'.png')
        }
    return Response(content=image_io, headers=headers, media_type='image/jpg')