#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from texts.API import API


class Izvestia(API):

    def parse_html(self, sql):
        for file in self.filename():
            with open(file, encoding='utf-8') as f:
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    try:
                        author = soup.find(property="article:author").attrs['content'].replace("'", '.')
                    except AttributeError:
                        author = ''
                    try:
                        date = soup.find(property="article:published_time").attrs['content'].replace("'", '.')
                    except AttributeError:
                        date = ''
                    try:
                        url = soup.find(property="og:url").attrs['content'].replace("'", '.')
                    except AttributeError:
                        url = ''
                    try:
                        header = soup.find(property="og:title").attrs['content'].replace("'", '.')
                    except AttributeError:
                        header = ''
                    try:
                        section = soup.find(property="article:section").attrs['content'].replace("'", '.')
                    except AttributeError:
                        section = ''
                    text = ''
                    for i in soup.findAll(itemprop="articleBody"):
                        text += i.text.strip().replace("'", '.') + '\n'

                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{3}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 3 AND LENGTH(TRANSCRIPT) > 100;", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
