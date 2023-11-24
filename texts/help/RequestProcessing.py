import asyncio
import aiohttp
from enum import Enum
from time import time, gmtime, strftime
import logging


class RequestResult(Enum):
    OK = '2'
    WRONG = '3'
    NOT_FOUND = '4'


class RequestProcessing:

    def __init__(self, url, user_agent, path, file_count):
        self._url = url
        self._user_agent = user_agent
        self._path = path
        self._file_count = file_count

    async def get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url) as response:
                html = await response.content.read()
                if str(response.status)[0] != RequestResult.OK.value:
                    return html
                return None

    async def write(self, response):
        try:
            with open(f'{self._path}/{self._file_count}.html', 'wb+') as f:
                f.write(response.content)
        except Exception as e:
            with open(f'{self._path}/err.txt', 'a+') as f:
                f.write(response.txt)
                f.write('\n\n\n')

    def __call__(self, *args, **kwargs):
        html = await self.get()
        await asyncio.sleep(0.5)
        if html:
            await self.write(html)
        await asyncio.sleep(0.5)
