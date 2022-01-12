import os

from fastapi import APIRouter

from main import config

router = APIRouter()

if not os.path.exists(config.wallpaper_collection_file_path):
    open(config.wallpaper_collection_file_path, 'w').close()
config.collections = []
with open(config.wallpaper_collection_file_path, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        config.collections.append(line)

import routes.wallpapers
import routes.search
import routes.random
import routes.main
import routes.collections
import routes.categories