<div align="center">
<h1>Wallpapers API</h1>

<img height="20px" src="https://forthebadge.com/images/badges/works-on-my-machine.svg">
<img height="20px" src="https://img.shields.io/badge/version-0.1.0-F05032?style=for-the-badge&logo=git">

An api which can use different sites to scrape images and serve them through API

**This API can be used for setting daily wallpapers on a mobile device by combining it with an app such as IFTTT**
</div>

## Installation

This is an ASGI server built using FastAPI. Here are some PaaS which is supported and you can deploy directly by clicking on the link below.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?repo=https://github.com/viperadnan-git/wallpaper-api)
<a href="https://go.deta.dev/deploy?repo=https://github.com/viperadnan-git/wallpaper-api">
    <img height="32" src="https://button.deta.dev/1/svg" alt="Deploy">
</a>

Or you can install it on your private server, the steps are given below.

### Installing Prerequisite
This project is written on python. Hence, install python-3.8.6 or later, see [`runtime.txt`](./runtime.txt) for exact version. 

On Ubuntu-18.04 or later
```sh
apt-get install -y python3 python3-pip
```

### Installing Python Packages
Install the required packages using pip
```sh
pip install -r requirements.txt
```

### Configuration

**Wallpaper website**

By default, it's scrapes wallpapers from <https://wallpapercave.com>. You can configure your desired wallpapers site's url and scraping regex in [`config.json`](./config.json)

**Collections**

This app uses collections name from [`collections.txt`](collections.txt) to fetch wallpapers from website and this list can be updated (as new collections arriving daily) by running the collection [`scraper`](scrape_collections.py). It have two modes, add collection from search or automaticaly fetch all collections.

_Note: Random wallpaper feature didn't work if collections file is empty so we added some nice collections already. You can remove file and add your own desired collections_
```sh
python3 scrape_collections.py
```
This will fetch and update the collection file automatically.

### Start Server
Start the ASGI server using **uvicorn**
```sh
uvicorn main:app
```

If using a VPS then set the host and port accordingly
```sh
uvicorn main:app --host 0.0.0.0 --port 80
```

[`Procfile`](./Procfile) already exists if you want to deploy it on railway or heroku etc.

## Copyright & License

Copyright (©) 2022 by [Adnan Ahmad](https://github.com/viperadnan-git).
Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)