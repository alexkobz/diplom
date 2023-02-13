# This Python file uses the following encoding: utf-8

import os
from API import *
from SQL import *


class Izvestia(API, SQL):
    def __init__(self, url=None, headers=None):
        if url is None:
            url = 'https://iz.ru/search?type=2&prd=3&from=0&text=%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F&date_from=2000-01-01&date_to=2005-04-19&sort=0'
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36 '
            }
        self.url = url
        self.headers = headers

    @SQL.connect
    def _api_get(self):
        url = self.url
        headers = self.headers
        node = 0
        while True:
            try:
                url_full = str(url[:39] + str(node) + url[39:])
                node += 1
                parsed_html = API(url_full, headers)._api_get(url_full, headers)
                if not parsed_html.find_all('div', attrs={'class': 'view-search__title'}):
                    break
                self.parse_html(parsed_html, headers)
            except Exception as e:
                with open(os.getcwd() + r'\\' + 'errors.txt', 'a') as txt:
                    txt.write(str(node) + '\t' + e.__str__() + '\n')

    @staticmethod
    def parse_html(parsed_html, headers):
        links = [link.a.get('href') for link in parsed_html.find_all('div', attrs={'class': 'view-search__title'})]
        dates = [date.string for date in parsed_html.find_all('div', attrs={'class': 'view-search__date'})]
        for link, date in zip(links, dates):
            try:
                article_parsed_html = API(link, headers)._api_get(link, headers)
                article_parsed_html_text = article_parsed_html.find('div', attrs={'class': 'text-article__inside'})
                article_text = article_parsed_html_text.find_all('p')
                if not article_text:
                    article_text = article_parsed_html_text.find('div', attrs={'itemprop': 'description'})
                tag_string = ''
                for tag in article_text:
                    tag_string += " ".join(tag.strings)
                date = date.replace(',', '')
                date_list = date.split()
                time = date_list[-1]
                date = '-'.join(date_list[:-1][::-1]).replace('января', '01').replace('февраля', '02').replace('марта', '03').replace('апреля', '04').replace('мая', '05').replace('июня', '06').replace('июля', '07').replace('августа', '08').replace('сентября', '09').replace('октября', '10').replace('ноября', '11').replace('декабря', '12').replace('г', '')
                SQL.insert(str(f"INSERT INTO IZVESTIA_TRANSCRIPTS VALUES ('{date}', '{time}', '{link}', '{tag_string}')"))
            except Exception as e:
                with open(os.getcwd() + r'\\' + 'errors.txt', 'a') as txt:
                    txt.write(str(link) + '\t' + e.__str__() + '\n')


    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, value='https://iz.ru/search?type=2&prd=0&from=0&text=%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F&date_from=2000-01-01&date_to=2021-09-16&sort=0'):
        self._url = value
    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value=None):
        if value is None:
            value = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36 '
            }
        self._headers = value
