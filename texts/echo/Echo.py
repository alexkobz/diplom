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
                    # sql.execute(
                    #     f"""INSERT INTO TRANSCRIPTS
                    #     (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE)
                    #     VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{1}');"""
                    # )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 1", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
