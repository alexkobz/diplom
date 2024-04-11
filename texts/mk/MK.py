#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from texts.API import API


class MK(API):

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    author = soup.find(class_="article__authors-data").find(itemprop="name").attrs['content']\
                        .replace("'", "`") if soup.find(class_="article__authors-data").find(itemprop="name") else ''
                    date = soup.find(class_="article__meta").find(itemprop="datePublished").attrs['content']\
                        .replace("'", "`") if soup.find(class_="article__meta").find(itemprop="datePublished") else ''
                    url = soup.find(property="og:url").attrs['content']\
                        .replace("'", "`") if soup.find(property="og:url") else ''
                    header = soup.find(name="title").text.strip()\
                        .replace("'", "`") if soup.find(name="title") else ''
                    section = soup.find(property="og:type").attrs['content']\
                        .replace("'", "`") if soup.find(property="og:type") else ''
                    text = ''
                    for i in soup.findAll(class_="article__body"):
                        text += i.text.strip() + '\n'
                    sql.execute(
                        f"""INSERT INTO MK_TRANSCRIPTS (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT)
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}')"""
                    )
                except:
                    pass
