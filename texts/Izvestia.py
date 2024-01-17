# This Python file uses the following encoding: utf-8

from texts.help.Media import Media
import os


class Izvestia(Media):
    pass
    # def get_known_urls(self):
    #     os.chdir(path=r'D:\diplom main')
    #
    #     urls = []
    #     with open(f'{self._basefolder}\iz_urls.txt', 'r') as f:
    #         urls = list(map(lambda x: x.replace('\n', ''), f.readlines()))
    #         print(urls[:100])
    #     return urls