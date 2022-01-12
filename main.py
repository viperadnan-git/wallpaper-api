import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


with open('config.json') as f:
    config = SimpleNamespace(**(json.loads(f.read())))

from routes import router

__version__ = "0.1.0"

description = """
**Wallpapers API**

All the wallpapers are fetched from <{api_url}>

**This API can be used for setting daily wallpapers on a mobile device by combining it with an app such as IFTTT**
""".format(api_url=config.wallpaper_api_url)

tags_metadata = [
    {
        "name": "Random Wallpapers",
        "description": "Returns a completely random wallpaper",
    },
    {
        "name": 'Collections',
        "description": "Working with collections, a collection contains wallpapers."
    },
    {
        "name": "Category",
        "description": "Workig with categories, a category contains collections"
    },
    {
        "name": "Search",
        "description": "Search for collections"
    },
    {
        'name': 'Wallpaper',
        'description': 'Get wallpaper by it\'s name'
    }
]

contact = {
    "name": "Adnan Ahmad",
    "url": "http://viperadnan-git.github.io",
    "email": "viperadnan@gmail.com",
}

app = FastAPI(
    title="Wallpapers API",
    description=description,
    version=__version__,
    contact=contact,
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url="/redocs",
)

app.mount("/static", StaticFiles(directory="web/static"), name="static")
app.include_router(router=router)
