from abc import abstractmethod
from csv import writer

from bs4 import BeautifulSoup

from interfaces.GetTextInterface import GetTextInterface as GTI
from interfaces.CountInterface import CountInterface as CI
from pandas import DataFrame
from requests import get, TooManyRedirects


class Text(GTI, CI):

    def __init__(self, basefolder, url, headers):
        self.basefolder = basefolder
        self.url = url
        self.headers = headers

    def api_get(self, url, headers) -> str:
        try:
            response = get(url, headers=headers)
            html = response.text
            parsed_html = BeautifulSoup(html, 'lxml')
            return parsed_html
        except ConnectionError:
            print('Connection Error')
        except TooManyRedirects:
            print('Too many redirects. URL may be invalid')
        except TimeoutError:
            print('Timeout. Try again later')

    @abstractmethod
    def parse_html(self, html) -> tuple:
        pass

    def write_txt_file(self, basefolder, filename, title, date, text):
        with open(basefolder + filename, mode='w', encoding='utf8') as file:
            file.write(title + '\n')
            file.write(str(date) + '\n')
            file.write(text + '\n')

    @abstractmethod
    def count(self, basefolder) -> DataFrame:
        pass

    def write_csv_file(self, basefolder, filename, counter):
        with open(basefolder + filename, mode='a', encoding='utf8', newline='') as file:
            csv_writer = writer(file, delimiter=';')
            row = (file[:-4], counter)
            csv_writer.writerow(row)

