#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from sql.SQL import SQL
from texts.API import API
from time import sleep
from waybackpy import WaybackMachineCDXServerAPI
import const.const as const


class Echo(API):

    async def __call__(self) -> None:
        self.mkdir()
        known_urls = self.get_known_urls()

        file_count = 1
        for url in known_urls:
            save_api = WaybackMachineCDXServerAPI(url, user_agent=const.USER_AGENT)
            archive_url = save_api.newest().archive_url
            try:
                await self.get_pages(archive_url, file_count)
                file_count += 1
                sleep(0.1)
            except:
                sleep(60)

    def parse_html(self, sql: SQL):
        for file in self.filename():
            with open(file, encoding='utf-8') as f:
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    sql.execute("""SELECT 1;"""
                        # f"""INSERT INTO ECHO_TRANSCRIPTS (HEADER, URL, TRANSCRIPT)
                        # VALUES('{header}','{url}', '{text}')"""
                    )
                except:
                    pass
