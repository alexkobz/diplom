#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from texts.API import API


class Zavtra(API):

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find(class_="avtor-name").text.strip()
                    date = soup.find(class_="header__data").text.strip()
                    url = soup.find(property="og:url").attrs['content']
                    header = soup.find(class_="header__title").text.strip()
                    section = soup.find(property="og:type").attrs['content']
                    text = ''
                    for i in soup.findAll(class_="article__content"):
                        text += i.text.strip() + '\n'
                    sql.execute(
                        f"""INSERT INTO ZAVTRA_TRANSCRIPTS (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT)
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}')"""
                    )
                except:
                    pass
