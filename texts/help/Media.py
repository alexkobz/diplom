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
        RequestProcessing(url, self._user_agent, self._basefolder, file_count)

    def get_known_urls(self):
        pattern = re.compile(self._pattern)
        urls = []
        known_urls = KnownUrls(self._url, self._user_agent).get_urls()
        for i in known_urls:
            if not re.search(pattern, i):
                continue
            urls.append(i)
            sleep(0.005)
        with open(f'{self._basefolder}/urls.txt', 'w') as f:
            f.writelines(urls)
        return (url for url in urls)


    def mkdir(self):
        try:
            os.mkdir(self._basefolder)
        except FileExistsError:
            print('FileExists')

    def __call__(self) -> None:
        self.mkdir()
        known_urls = self.get_known_urls()

        file_count = 1
        for url in known_urls:
            try:
                self.get_pages(url, file_count)
                file_count += 1
                sleep(0.1)
            except:
                sleep(self._timeout + 1)
