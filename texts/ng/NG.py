#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from texts.API import API


class NG(API):

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find(class_="author").text.strip().replace("'", '.') if soup.find(
                        class_="author") else ''
                    date = soup.find(class_="info").text.strip().replace("'", '.') if soup.find(class_="info") else ''
                    url = soup.find(property="og:url").attrs['content'].replace("'", '.') if soup.find(
                        property="og:url") else ''
                    try:
                        header = soup.find(property="og:title").attrs['content'].replace("'", '.')
                    except:
                        header = ''
                    try:
                        section = soup.find(property="og:type").attrs['content'].replace("'", '.')
                    except:
                        section = ''
                    text = ''
                    for i in soup.findAll(class_="typical"):
                        text += i.text.strip().replace("'", '.') + '\n'
                    sql.execute(
                        f"""INSERT INTO NG_TRANSCRIPTS (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT)
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}')"""
                    )
                except:
                    pass
