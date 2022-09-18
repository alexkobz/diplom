import requests
from bs4 import BeautifulSoup


def get_text(url):
    rs = requests.get(url)
    # root = BeautifulSoup(rs.content, 'html.parser')
    # article = root.select_one('article')
    # print(root)
    # return article.text


url = 'http://transcript.duma.gov.ru/node/2264/'

rs = requests.get(url)
print(rs.text)
# text = get_text(url)
# print(text)
# print(text[:100])  # Первые 100 символов из строки