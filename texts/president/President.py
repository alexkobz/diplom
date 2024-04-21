#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import re
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from texts.API import API
from texts.KnownUrls import KnownUrls


class President(API):

    def save_urls(self):
        self.mkdir()
        known_urls = KnownUrls(self._url).get_urls()
        pattern_transcripts = re.compile(r'\S+events/president/transcripts/\d+$')
        pattern_news = re.compile(r'\S+events/president/news/\d+$')
        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'a+') as f:
            for url in known_urls:
                url = url.replace('%20', '')
                if pattern_transcripts.match(url) or pattern_news.match(url):
                    f.write(url)
            sleep(1)

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = ""
                    date = soup.find(class_="read__published").attrs['datetime']
                    url = soup.find(property="og:url").attrs['content']
                    header = soup.find(property="og:title").attrs['content']
                    section = ''
                    text = soup.find(itemprop="articleBody").text
                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{7}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 7", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
