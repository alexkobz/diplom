#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from texts.API import API


class Kommersant(API):

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find('article')['data-analytics-authors'].replace("'", "`") if soup.find('article') else ''
                    date = soup.find('article')['data-article-daterfc822'].replace("'", "`") if soup.find('article') else ''
                    url = soup.find('article')['data-canonical-url'].replace("'", "`") if soup.find('article') else ''
                    header = soup.find('article')['data-canonical-title'].replace("'", "`") if soup.find('article') else ''
                    section = ''
                    text = soup.find('div', itemprop="articleBody").text.replace('\n', ' ').replace("'", "`").strip() if soup.find('div', itemprop="articleBody") else ''
                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{4}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 4", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
