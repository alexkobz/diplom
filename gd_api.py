import os
import csv
import requests
from bs4 import BeautifulSoup


def api(nodes, path):

    for node in nodes:

        url = f'http://transcript.duma.gov.ru/node/{str(node)}/'
        response = requests.get(url)  # 'Content-Type': 'text/html; charset=UTF-8'
        if response.status_code != 200:
            continue
        html = response.text
        parsed_html = BeautifulSoup(html, 'lxml')
        header = parsed_html.body.find('div', attrs={'class': 'header-bord'}).text.replace('\n', ' ')
        header_list = header.split()
        if header_list[0] == 'Стенограмма':
            header = ' '.join(header_list[2:-4])
            transcript = parsed_html.body.find('div', attrs={'id': 'selectable-content'}).text
            with open(path + '\\' + str(header) + '.txt', 'w') as file:
                file.write(transcript)


def count(path):

    democracy = 'демократ'

    for root, dirs, files in os.walk(path, topdown=False):
        if root[-1].isdigit():
            f = open(root + '\\' + 'count.csv', 'w')
            f.close()
        for file in files:

            if file[:-4] == '.csv':
                continue
            counter = 0
            with open(root + '\\' + file, 'r') as txt:
                transcript = txt.read()
            transcript_list = transcript.split()

            for word in transcript_list:
                if democracy in word:
                    counter += 1

            if counter:
                with open(root + '\\' + 'count.csv', 'a+', encoding='utf8', newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';')
                    row = (file, counter)
                    writer.writerow(row)


def main():

    basefolder = r'C:\Users\kobzaale\Desktop\diplom'

    # 18 января 2000 г. - 22 октября 2010 г.
    nodes_reverse = range(2265, 43, -1)

    # 01 ноября 2010 г. - 17 июня 2021 г.
    nodes = range(3332, 3341)

    try:
        api(nodes_reverse, basefolder)
        api(nodes, basefolder)
    except ConnectionError:
        print('ConnectionError')
    except AttributeError:
        print('AttributeError')

    try:
        count(basefolder)
    except FileNotFoundError:
        print('FileNotFoundError')


if __name__ == '__main__':
    main()
