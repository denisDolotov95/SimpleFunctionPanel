# -*- coding: utf-8 -*-
import re
import logging
import redis.asyncio
import redis.exceptions
import asyncpg
import urllib3
import aiohttp

from typing import Any
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import create_async_engine

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FormatData(BaseModel):

    ip: str = Field(pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    url: str = Field()
    status: int | None = Field()


class AgregateData:

    ip = lambda self, x: re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", x)[0]
    port = lambda self, x: re.findall(r":\d{1,3}", x)[0]

    @staticmethod
    async def http_requset(url: str) -> int | None:

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, verify_ssl=False, timeout=1) as response:
                    return response.status
        except Exception as err:
            logging.error(f"{err}")
            return

    @staticmethod
    async def db_requset(url: str):
        """Проверка доступа до узла баз данных

        Args:
            url (str): _description_

        Returns:
            _type_: _description_
        """

        try:
            engine = create_async_engine(url)
            await engine.connect()
            return True
        except asyncpg.exceptions.PostgresError as err:
            if "no pg_hba.conf entry for host" in str(err):
                return True
            return False

    @staticmethod
    async def check_redis(_ip: str):

        try:
            r = await redis.asyncio.Redis(host=_ip, socket_connect_timeout=1)
            return await r.ping()
        except redis.exceptions.TimeoutError:
            return False

    def __init__(self, *args, **kwargs):
        self.urls: dict = kwargs

    def format_data(f):
        async def wrapper(*args, **kwargs):
            data = await f(*args, **kwargs)
            ip, url, status = data
            return FormatData(ip=ip, url=url, status=status)

        return wrapper

    @format_data
    async def get_status_portainer(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("portainer")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status

    @format_data
    async def get_status_grafana(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("grafana")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status

    @format_data
    async def get_status_prometheus(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("prometheus")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status

    @format_data
    async def get_status_gate_api(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("gate_api")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status

    @format_data
    async def get_status_rabbit_mq(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("rabbit_mq")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status

    @format_data
    async def get_status_psql(self, key: str) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get(key)
        ip = self.ip(url)
        status = await self.db_requset(url)
        return ip, url, status

    @format_data
    async def get_status_redis(self) -> tuple[Any, Any | None, Any | None]:

        url = self.urls.get("redis")
        ip = self.ip(url)
        status = await self.http_requset(url)
        return ip, url, status
