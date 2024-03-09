import os
from texts.help.KnownUrls import KnownUrls
from texts.help.RequestProcessing import RequestProcessing
from time import sleep
import asyncio


class API:

    def __init__(self, url):
        self._url = url
        self._basefolder = self.__class__.__name__.lower()

    async def get_pages(self, url, file_count):
        rp = RequestProcessing(url, self._basefolder, file_count)
        await rp()

    def mkdir(self):
        os.chdir(path=r'D:\diplom main')
        try:
            os.mkdir(self._basefolder)
        except FileExistsError:
            print(f'{self._basefolder} folder exists')

    def save_urls(self):
        self.mkdir()
        known_urls = KnownUrls(self._url).get_urls()
        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'a+') as f:
            for url in known_urls:
                url = url.replace('%20', '')
                f.write(url)
            sleep(1)

    def get_known_urls(self):
        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'r') as f:
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
