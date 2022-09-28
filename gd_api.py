import os
import csv
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


def analyze(path):

    df_common = pd.DataFrame()

    fig, ax = plt.subplots()

    for convocation in range(3, 8):

        df = pd.read_csv(path + '\\' + 'gd' + '\\' + str(convocation) + '\\' + 'count.csv',
                         delimiter=';', names=['Date', 'Count'])
        df = df \
            .replace('.января.', '/01/', regex=True) \
            .replace('.февраля.', '/02/', regex=True) \
            .replace('.марта.', '/03/', regex=True) \
            .replace('.апреля.', '/04/', regex=True) \
            .replace('.мая.', '/05/', regex=True) \
            .replace('.июня.', '/06/', regex=True) \
            .replace('.июля.', '/07/', regex=True) \
            .replace('.августа.', '/08/', regex=True) \
            .replace('.сентября.', '/09/', regex=True) \
            .replace('.октября.', '/10/', regex=True) \
            .replace('.ноября.', '/11/', regex=True) \
            .replace('.декабря.', '/12/', regex=True) \
            .replace('г', '', regex=True)
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
        df.sort_values(by='Date', inplace=True)

        year_df = df \
            .groupby(df['Date'].dt.year) \
            .sum()
        year_df = year_df.reset_index()
        df_common = df_common.append(year_df)

        agg_df = df \
            .groupby([df['Date'].dt.year, df['Date'].dt.month]) \
            .sum()
        agg_df.index.names = ['Year', 'Month']
        agg_df = agg_df.reset_index()
        agg_df['Period'] = agg_df['Year'].astype(str) + '-' + agg_df['Month'].astype(str)
        agg_df = agg_df.drop(columns=['Year', 'Month'])

        x = agg_df['Period']
        y = agg_df['Count']
        ax.plot(x, y, linewidth=2.0, marker='.')
        fig.suptitle(f'{convocation} convocations', fontsize=20)
        plt.xticks(rotation=90)
        plt.ylabel('Count', fontsize=10)
        plt.grid(True)

        x_trend = np.array(range(len(x)))
        y_trend = np.array(y)
        z = np.polyfit(x_trend, y_trend, 1)
        p = np.poly1d(z)
        plt.plot(x_trend, p(x_trend), "r--")

    x = df_common['Date']
    y = df_common['Count']
    ax.plot(x, y, linewidth=2.0, marker='.')
    # ax.set_facecolor('yellow')
    # ax.patch.set_alpha(0.2)
    fig.suptitle('3-7 convocations', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Count', fontsize=10)
    plt.grid(True)

    x_trend = np.array(x)
    y_trend = np.array(y)
    z = np.polyfit(x_trend, y_trend, 1)
    p = np.poly1d(z)
    plt.plot(x_trend, p(x_trend), "r--")

    plt.show()


def izvestia(path):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36 '
    }

    c = 1
    for i in range(408):
        url = f'https://iz.ru/search?type=2&prd=3&from={str(i)}0&text=%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F&date_from=2000-01-01&date_to=2011-04-16&sort=0'
        response = requests.get(url, headers=headers)
        html = response.text
        parsed_html = BeautifulSoup(html, 'lxml')
        articles = parsed_html.body.findAll('div', attrs={'class': 'view-search__title'})
        for article in articles:
            tag = article.find('a')
            article_url = tag.get('href')
            article_response = requests.get(article_url, headers=headers)
            article_html = article_response.text
            article_parsed_html = BeautifulSoup(article_html, 'lxml')
            try:
                article_title = article_parsed_html.body.find('div', attrs={'itemprop': 'name'}).text
                header_list = article_title.split()
                header = ' '.join(header_list)
                article_date = article_parsed_html.body.find('div', attrs={'itemprop': 'datePublished'}).text
                article_description_html = article_parsed_html.body.find('div', attrs={'class': 'text-article__inside'})
                tag = article_description_html.find('div')
                article_text = tag.find('div').text

                with open(path + '\\' + 'smi' + '\\' + 'izvestia' + '\\' + str(c) + '.txt', 'w', encoding='utf8') as file:
                    file.write(article_url)
                    file.write('\n')
                    file.write(header)
                    file.write('\n')
                    file.write(article_date)
                    file.write('\n')
                    file.write(article_text)
            except AttributeError:
                continue

        c += 1


def main():

    basefolder = r'C:\Users\kobzaale\Desktop\diplom'
    #
    # # 18 января 2000 г. - 22 октября 2010 г.
    # nodes_reverse = range(2265, 43, -1)
    #
    # # 01 ноября 2010 г. - 17 июня 2021 г.
    # nodes = range(3332, 3341)
    #
    # try:
    #     api(nodes_reverse, basefolder)
    #     api(nodes, basefolder)
    # except ConnectionError:
    #     print('ConnectionError')
    # except AttributeError:
    #     print('AttributeError')
    #
    # #
    # # Manually sort txt files by convocations. Then run code below
    # #
    # # 3rd convocation: 2000 - 2003
    # # 4th convocation: 2004 - 2007
    # # 5th convocation: 2008 - 2011
    # # 6th convocation: 2012 - 2016
    # # 7th convocation: 2017 - 2021
    # #
    #
    # try:
    #     count(basefolder)
    # except FileNotFoundError:
    #     print('FileNotFoundError')

    # analyze(basefolder)

    izvestia(basefolder)


if __name__ == '__main__':
    main()
