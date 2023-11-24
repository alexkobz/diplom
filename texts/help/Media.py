import os
from texts.help.KnownUrls import KnownUrls
from texts.help.RequestProcessing import RequestProcessing
from time import sleep
import re


class Media:

    def __init__(self, url, user_agent, basefolder, timeout, pattern):
        self._url = url
        self._user_agent = user_agent
        self._basefolder = basefolder
        self._timeout = timeout
        self._pattern = pattern

    @property
    def basefolder(self):
        return self._basefolder

    @basefolder.setter
    def basefolder(self, basefolder):
        self._basefolder = basefolder

    def get_pages(self, url, file_count):
        rp = RequestProcessing(url, self._user_agent, self._basefolder, file_count)
        rp()

    def get_known_urls(self):

        urls = []
        with open(f'{self._basefolder}\{self._basefolder}_urls.txt', 'r') as f:
            urls = f.read().splitlines()
        return (url for url in urls)


    def mkdir(self):
        try:
            os.mkdir(self._basefolder)
        except FileExistsError:
            print(f'{self._basefolder} folder exists')

    async def __call__(self) -> None:
        os.chdir(path=r'D:\diplom main')
        self.mkdir()
        known_urls = self.get_known_urls()

        file_count = 1
        for url in known_urls:
            try:
                self.get_pages(url, file_count)
                file_count += 1
                sleep(0.01)
                # if file_count >= 100:
                #     break
            except:
                sleep(self._timeout + 1)
