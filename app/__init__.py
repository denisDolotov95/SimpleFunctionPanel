# -*- coding: utf-8 -*-
import logging

from logging.handlers import RotatingFileHandler
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape

import config

for log in (logging.getLogger(n) for n in logging.root.manager.loggerDict):
    log.setLevel(logging.DEBUG)


rot_file_handler = RotatingFileHandler(f"web.log",
                                       maxBytes=10*1024*1024,
                                       backupCount=3,
                                       encoding="utf-8")

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[rot_file_handler],
    format='[%(asctime)s] (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"')

app_config = config.ProductionConfig()

app = FastAPI()

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
jinja_env = Environment(loader=PackageLoader('app', 'templates'),
                        autoescape=select_autoescape(['html', 'xml']))
# templates = Jinja2Templates(directory="./app/templates")

from .routes import *