#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import asyncio
import os
import pandas as pd
from bs4 import BeautifulSoup
from texts.API import API
from sql.SQL import SQL


class GosDuma(API):

    def save_urls(self):
        self.mkdir()
        # 18 января 2000 г. - 22 октября 2010 г.
        nodes_reverse = list(range(407, 43, -1))

        # 01 ноября 2010 г. - 17 июня 2021 г.
        nodes_straight = list(range(3332, 5686))

        nodes = nodes_reverse + nodes_straight

        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'w+') as f:
            f.writelines([self._url + str(node) + '\n' for node in nodes])

    async def __call__(self) -> None:
        os.chdir(path=r'./web pages')
        known_urls = self.get_known_urls()
        for url in known_urls:
            file_count = url.split("/")[-2]
            try:
                await self.get_pages(url.replace('\n', '').replace('%20', ''), file_count)
            except:
                await asyncio.sleep(60)

    def parse_html(self, sql: SQL):
        for file in self.filename():
            with open(file, encoding='utf-8') as f:
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = ''
                    date = soup.find('head').find('title').text.replace("'", "`")
                    url = self._url + str(file).replace(".html", "")
                    header = ''
                    section = ''
                    text = "\n".join([str(i).replace('<p>', '').replace('</p>', '').replace("'", "`")
                                      for i in soup.find(id='selectable-content').findAll('p')])
                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{2}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 2", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
