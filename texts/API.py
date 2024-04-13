#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import os
import asyncio
import pandas as pd
from time import sleep
from abc import ABC, abstractmethod
from texts.KnownUrls import KnownUrls
from texts.RequestProcessing import RequestProcessing
from sql.SQL import SQL
from texts.text_cleaner import text_cleaner


class API(ABC):

    def __init__(self, url):
        self._url = url
        self._basefolder = self.__class__.__name__.lower()

    async def get_pages(self, url, file_count):
        rp = RequestProcessing(url, self._basefolder, file_count)
        await rp()

    def mkdir(self):
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
        os.chdir(path=r'./web pages')
        known_urls = self.get_known_urls()
        file_count = 1
        for url in known_urls:
            try:
                await self.get_pages(url.replace('\n', '').replace('%20', ''), file_count)
                file_count += 1
            except:
                await asyncio.sleep(60)

    def filename(self):
        for _, _, files in os.walk(self._basefolder):
            for file in files:
                yield file

    @abstractmethod
    def parse_html(self, sql: SQL):
        pass

    @abstractmethod
    def cast_date(self, sql: SQL) -> pd.DataFrame:
        pass

    def clean_text(self, sql: SQL):
        df = self.cast_date(sql)
        df0021 = df[(df.DDATE >= "2000-01-01") & (df.DDATE <= "2021-09-17")]
        df0021["CLEAN_TEXT"] = df0021["TRANSCRIPT"].apply(text_cleaner)
        df0021["DEMOCRACY_COUNT"] = df0021["CLEAN_TEXT"].apply(lambda text: text.count("демократия"))
        df0021.to_sql(f"{self.__class__.__name__.upper()}0021", sql.__CONNECTION)
