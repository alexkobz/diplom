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
                        f"""INSERT INTO TRANSCRIPTS 
                        (AUTHOR, DDATE, URL, HEADER, SECTION, FILENAME, TRANSCRIPT, SOURCE) 
                        VALUES('{author}', '{date}', '{url}', '{header}', '{section}', '{file}', '{text}', '{9}');"""
                    )
                except:
                    pass

    def cast_date(self, sql):
        def date_replace(d):
            return d.replace("января", "01").replace("февраля", "02").replace("марта", "03").replace("апреля", "04")\
            .replace("мая", "05").replace("июня", "06").replace("июля", "07").replace("августа", "08")\
            .replace("сентября", "09").replace("октября", "10").replace("ноября", "11").replace("декабря", "12")
            
        df = pd.read_sql("SELECT * FROM TRANSCRIPTS WHERE SOURCE = 9", sql.__CONNECTION)
        df["DDATE"] = df["DDATE"].apply(date_replace)
        df["DDATE"] = pd.to_datetime(df["DDATE"], format='%d %m %Y')
        return df
