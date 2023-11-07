# This Python file uses the following encoding: utf-8

from bs4 import BeautifulSoup
from requests import get


class API:
    def __init__(self, url, headers=''):
        self._url = url
        self._headers = headers

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers

    @staticmethod
    def _api_get(url=str(url), headers=headers) -> BeautifulSoup:
        try:
            response = get(url, headers=headers)
            html = response.text
            parsed_html = BeautifulSoup(html, 'html.parser')
            return parsed_html
        except Exception as e:
            print(e.__str__())
