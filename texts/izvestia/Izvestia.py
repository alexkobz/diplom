# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
from sql.SQL import SQL
from texts.API import API


class Izvestia(API):

    def parse_html(self):
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

                    SQL.execute(
                        f"""INSERT INTO IZVESTIA_TRANSCRIPTS_NEW (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}');"""
                    )
                except:
                    pass
