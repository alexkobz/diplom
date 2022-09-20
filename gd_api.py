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
        header_list = header_list[2:-4]
        header_list = header_list[:3]
        if header_list[0] == 'Стенограмма':
            header = ' '.join(header_list)
            transcript = parsed_html.body.find('div', attrs={'id': 'selectable-content'}).text
            with open(path + '\\' + str(header) + '.txt', 'w') as file:
                file.write(transcript)

        duma = os.path.join(path, 'gd')
        os.mkdir(duma)
        for f in range(3, 8):
            convocation = os.path.join(duma, str(f))
            os.mkdir(convocation)
            convocation_archive = os.path.join(convocation, 'archive')
            os.mkdir(convocation_archive)


def count(path):

    democracy = 'демократ'

    for root, dirs, files in os.walk(path, topdown=False):
        if root[-1].isdigit():
            f = open(root + '\\' + 'count.csv', 'w')
            f.close()
        for file in files:
            if file[-4:] == '.csv':
                continue

            counter = 0
            with open(root + '\\' + file, 'r') as txt:
                transcript = txt.read()
            transcript_list = transcript.lower().split()

            for word in transcript_list:
                if democracy in word and 'либерально-демократ' not in word:
                    counter += 1

            if counter:
                with open(root + '\\' + 'count.csv', 'a+', encoding='utf8', newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';')
                    row = (file[:-4], counter)
                    writer.writerow(row)
            else:
                os.rename(root + '\\' + file, root + '\\' + 'archive\\' + file)


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

    #
    # Manually sort txt files by convocations. Then run code below
    #
    # 3rd convocation: 2000 - 2003
    # 4th convocation: 2004 - 2007
    # 5th convocation: 2008 - 2011
    # 6th convocation: 2012 - 2016
    # 7th convocation: 2017 - 2021
    #

    try:
        count(basefolder)
    except FileNotFoundError:
        print('FileNotFoundError')


if __name__ == '__main__':
    main()
