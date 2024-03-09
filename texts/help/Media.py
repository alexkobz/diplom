import os
from texts.help.KnownUrls import KnownUrls
from texts.help.RequestProcessing import RequestProcessing
from time import sleep
import asyncio


class Media:

    def __init__(self, url, basefolder, timeout):
        self._url = url
        self._basefolder = basefolder
        self._timeout = timeout

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
            sleep(0.001)

    def get_known_urls(self):
        with open(f'{self._basefolder}\{self._basefolder}_urls.txt', 'r') as f:
            for url in f:
                yield url

    async def __call__(self) -> None:
        os.chdir(path=r'E:\diplom\web pages')
        known_urls = self.get_known_urls()
        file_count = 1
        for url in known_urls:
            try:
                await self.get_pages(url.replace('\n', '').replace('%20', ''), file_count)
                file_count += 1
            except Exception as e:
                await asyncio.sleep(self._timeout + 1)
                # print(e)