# This Python file uses the following encoding: utf-8

import os
from texts.help.API import API
from const.const import USER_AGENT
from texts.help.RequestProcessing import RequestProcessing
from time import sleep


class GosDuma(API):

    def __call__(self):
        os.chdir(path=r'./web pages')
        GosDuma._api_get(self)


    async def _api_get(self):
        # 18 января 2000 г. - 22 октября 2010 г.
        nodes_reverse = list(range(407, 43, -1))

        # 01 ноября 2010 г. - 17 июня 2021 г.
        nodes_straight = list(range(3332, 5686))

        nodes = nodes_reverse + nodes_straight
        for node in nodes:
            url = self.__URL + str(node)
            try:
                rp = RequestProcessing(url, "gosduma", str(node))
                await rp()
            except Exception:
                sleep(60)
