from texts.help.API import API
from time import sleep
import re
import os


class Kommersant(API):
    pass
    # def get_known_urls(self):
    #
    #     urls = []
    #     with open(f'{self._basefolder}\kommersant_urls.txt', 'r') as f:
    #         urls = f.read().splitlines()
    #     return urls
        # known_urls = super().get_known_urls()
        # pattern = re.compile('oc/\d*$')
        # kommersant_urls = []
        # for i in known_urls:
        #     if not re.search(pattern, i):
        #         continue
        #     kommersant_urls.append(i)
        #     sleep(0.005)
        # with open(f'{super()._basefolder}/urls.txt', 'w') as f:
        #     f.writelines(kommersant_urls)
        # return (url for url in kommersant_urls)
