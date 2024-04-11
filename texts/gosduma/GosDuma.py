#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import asyncio
import os
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
                    url = self._url + str(file).replace(".html", "")
                    header = soup.find('head').find('title').text.replace("'", "`")
                    text = "\n".join([str(i).replace('<p>', '').replace('</p>', '').replace("'", "`")
                                      for i in soup.find(id='selectable-content').findAll('p')])
                    sql.execute(
                        f"""INSERT INTO GD_TRANSCRIPTS (HEADER, URL, TRANSCRIPT)
                        VALUES('{header}','{url}', '{text}')"""
                    )
                except:
                    pass
