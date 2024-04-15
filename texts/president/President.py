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
        pattern = re.compile(r'\S+events/president/transcripts/\d+$')
        with open(f'{self._basefolder}\\{self._basefolder}_urls.txt', 'a+') as f:
            for url in known_urls:
                url = url.replace('%20', '')
                if pattern.match(url):
                    f.write(url)
            sleep(1)

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find('article')['data-analytics-authors'].replace("'", "`") if soup.find(
                        'article') else ''
                    date = soup.find('article')['data-article-daterfc822'].replace("'", "`") if soup.find(
                        'article') else ''
                    url = soup.find('article')['data-canonical-url'].replace("'", "`") if soup.find('article') else ''
                    header = soup.find('article')['data-canonical-title'].replace("'", "`") if soup.find(
                        'article') else ''
                    section = ''
                    text = soup.find('div', itemprop="articleBody").text.replace('\n', ' ').replace("'",
                                                                                                    "`").strip() if soup.find(
                        'div', itemprop="articleBody") else ''
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
