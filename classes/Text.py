from csv import writer
from bs4 import BeautifulSoup
from interfaces.GetTextInterface import GetTextInterface as GTI
from interfaces.CountInterface import CountInterface as CI
from interfaces.AnalyzeInterface import AnalyzeInterface as AI
from requests import get, TooManyRedirects


class Text(GTI, CI, AI):

    __HEADERS = {'User-Agent': 'Chrome/35.0.1916.47'}

    def __init__(self, basefolder, url):
        self.__basefolder = basefolder
        self.__url = url

    @property
    def basefolder(self):
        return self.__basefolder

    @property
    def url(self):
        return self.__url

    def api_get(self, url) -> BeautifulSoup:
        try:
            response = get(url, headers=Text.__HEADERS)
            html = response.text
            parsed_html = BeautifulSoup(html, 'lxml')
            return parsed_html
        except ConnectionError:
            print('Connection Error')
        except TooManyRedirects:
            print('Too many redirects. URL may be invalid')
        except TimeoutError:
            print('Timeout. Try again later')

    def write_txt_file(self, basefolder, filename, title, date, text):
        with open(basefolder + filename, mode='w', encoding='utf8') as file:
            file.write(title + '\n')
            file.write(str(date) + '\n')
            file.write(text + '\n')

    def write_csv_file(self, basefolder, filename, counter):
        with open(basefolder + filename, mode='a', encoding='utf8', newline='') as file:
            csv_writer = writer(file, delimiter=';')
            row = (file[:-4], counter)
            csv_writer.writerow(row)
