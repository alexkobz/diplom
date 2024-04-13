#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import json
from bs4 import BeautifulSoup
from texts.API import API


class Vedomosti(API):

    def parse_html(self, sql):
        for file in self.filename():
            with (open(file, encoding='utf-8') as f):
                try:
                    html = f.read()
                    soup = BeautifulSoup(html)
                    try:
                        author = json.loads(soup.find(type="application/ld+json").text)['author'][0]['name']\
                            .replace("'", '`')
                    except:
                        pass
                    date = json.loads(soup.find(type="application/ld+json").text)['datePublished']\
                        .replace("'", '`') if soup.find(type="application/ld+json") else ''
                    url = json.loads(soup.find(type="application/ld+json").text)['url']\
                        .replace("'", '`') if soup.find(type="application/ld+json") else ''
                    try:
                        header = json.loads(soup.find(type="application/ld+json").text)['description'].replace("'", '`')
                    except:
                        header = ''
                    try:
                        section = json.loads(soup.find(type="application/ld+json").text)['articleSection']\
                            .replace("'", '`')
                    except:
                        section = ''
                    text = ''
                    for i in soup.findAll(class_="box-paragraph__text"):
                        text += i.text.strip().replace("'", '.') + '\n'
                    sql.execute(
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{8}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 8", sql.__CONNECTION)
        df["DDATE"] = pd.to_datetime(df["DDATE"]).dt.tz_localize(None)
        return df
