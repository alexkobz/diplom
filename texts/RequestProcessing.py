import asyncio
import aiohttp
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import const.const as const
from logger.Logger import Logger

logger = Logger()

class RequestProcessing:

    user_agent = const.USER_AGENT

    def __init__(self, url, path, file_count):
        self._url = url
        self._path = path
        self._file_count = file_count

    async def get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url, headers=RequestProcessing.user_agent) as response:
                html = await response.content.read()
                if response.ok:
                    return html
                return None

    async def write(self, response):
        try:
            with open(f'{self._path}/{self._file_count}.html', 'wb+') as f:
                f.write(response)
        except Exception as e:
            with open(f'{self._path}/err.txt', 'a+') as f:
                f.write(response)
                f.write('\n\n\n')

    async def __call__(self, *args, **kwargs):
        html = await self.get()
        await asyncio.sleep(0.5)
        if html:
            await self.write(html)
        await asyncio.sleep(0.5)
