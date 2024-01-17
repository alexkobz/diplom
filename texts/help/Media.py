import os
import sys

from texts.help.KnownUrls import KnownUrls
from texts.help.RequestProcessing import RequestProcessing
from time import sleep
import re
import asyncio


class Media:

    def __init__(self, url, basefolder, timeout, pattern):
        self._url = url
        self._basefolder = basefolder
        self._timeout = timeout
        self._pattern = pattern

    @property
    def basefolder(self):
        return self._basefolder

    @basefolder.setter
    def basefolder(self, basefolder):
        self._basefolder = basefolder

    async def get_pages(self, url, file_count):
        rp = RequestProcessing(url, self._basefolder, file_count)
        await rp()
        # print(self._basefolder)
        # await asyncio.sleep(2)
        # print('ready')

    def mkdir(self):
        os.chdir(path=r'D:\diplom main')
        try:
            os.mkdir(self._basefolder)
        except FileExistsError:
            print(f'{self._basefolder} folder exists')

    def save_urls(self):
        self.mkdir()
        known_urls = KnownUrls(self._url).get_urls()
        for url in known_urls:
            url = url.replace('%20', '')
            if re.search(self._pattern, url):
                with open(f'{self._basefolder}/{self._basefolder}_urls.txt', 'a+') as f:
                    f.write(url + '\n')
            sleep(0.001)

    def get_known_urls(self):
        with open(f'{self._basefolder}\{self._basefolder}_urls.txt', 'r') as f:
            for url in f:
                yield url
    # async def c(self):
    #     print(self._basefolder)
    #     await asyncio.sleep(3)
    #     print(self._basefolder, '2')


    # async def call(self) -> None:
    async def __call__(self) -> None:
        # print(self._basefolder)
        # await asyncio.sleep(3)
        # print(self._basefolder, '2')
        # task = asyncio.create_task(self.c())
        # await task
        os.chdir(path=r'E:\diplom\web pages')
        known_urls = self.get_known_urls()
        # for i in known_urls:
        #     print(i)
        #     await asyncio.sleep(2)
        #     sys.exit(1)
        # print(known_urls)
        # sys.exit(1)
        file_count = 1
        for url in known_urls:
            try:
                await self.get_pages(url.replace('\n', '').replace('%20', ''), file_count)
                file_count += 1
            except Exception as e:
                await asyncio.sleep(self._timeout + 1)
                # print(e)