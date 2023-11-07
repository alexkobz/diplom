# This Python file uses the following encoding: utf-8

import os
from texts.help.API import *
from sql.SQL import *
from itertools import chain


class GosDuma(API):
    
    __URL = 'http://transcript.duma.gov.ru/node/'
    __HEADERS = ''

    def __init__(self):
        super().__init__(GosDuma.__URL, GosDuma.__HEADERS)

    def __call__(self):
        GosDuma._api_get(self)

    def _api_get(self):
        # 18 января 2000 г. - 22 октября 2010 г.
        nodes_reverse = range(407, 43, -1)

        # 01 ноября 2010 г. - 17 июня 2021 г.
        nodes_straight = range(3332, 5686)

        nodes = chain(nodes_reverse, nodes_straight)
        url = self.__URL
        headers = self.__HEADERS
        for node in nodes:
            try:
                url_full = f'{url}{str(node)}/'
                parsed_html = super()._api_get(url_full, headers)
                self.parse_html(parsed_html, url_full)
            except Exception as e:
                with open(os.getcwd() + r'\\' + 'errors.txt', 'a') as txt:
                    txt.write(str(node) + '\t' + str(e) + '\n')

    @staticmethod
    @SQL.connect
    def parse_html(parsed_html, url):
        header = parsed_html.find('div', attrs={'class': 'header-bord'}).text.replace('\n', ' ')
        header_list = header.split()
        if header_list[0] == 'Стенограмма':
            date = '-'.join(header_list[2:5][::-1]) \
                .replace('января', '01') \
                .replace('февраля', '02') \
                .replace('марта', '03') \
                .replace('апреля', '04') \
                .replace('мая', '05') \
                .replace('июня', '06') \
                .replace('июля', '07') \
                .replace('августа', '08') \
                .replace('сентября', '09') \
                .replace('октября', '10') \
                .replace('ноября', '11') \
                .replace('декабря', '12') \
                .replace('г', '')
            transcript = parsed_html.body.find('div', attrs={'id': 'selectable-content'}).text.replace('\'', '')
            SQL.insert(str(f"INSERT INTO GD_TRANSCRIPTS VALUES ('{date}', '{url}', '{transcript}')"))
