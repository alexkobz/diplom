import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from classes.Text import Text


class StateDuma(Text):

    def parse_html(self, html) -> tuple[str, str, str, str]:
        header = html.body.find('div', attrs={'class': 'header-bord'}).text.replace('\n', ' ')
        header_list = header.split()
        if header_list[0] == 'Стенограмма':
            header_list = header_list[2:]
            header_list = header_list[:3]
            title = ' '.join(header_list)
            transcript = html.body.find('div', attrs={'id': 'selectable-content'}).text
            return f'{title}.txt', title, title, transcript
        return '', '', '', ''

    def count(self, basefolder):

        democracy = 'демократ'

        for root, dirs, files in os.walk(basefolder, topdown=False):
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
                    Text.write_csv_file(self, basefolder, file, counter)
                else:
                    os.rename(root + '\\' + file, root + '\\' + 'archive\\' + file)

    def analyze(self, basefolder):

        df_common = pd.DataFrame()

        fig, ax = plt.subplots()

        for convocation in range(3, 8):
            df = pd.read_csv(basefolder + '\\' + 'gd' + '\\' + str(convocation) + '\\' + 'count.csv',
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

    def __call__(self, basefolder, url):

        # # 18 января 2000 г. - 22 октября 2010 г.
        # nodes_desc = range(2265, 43, -1)
        #
        # # 01 ноября 2010 г. - 17 июня 2021 г.
        # nodes_asc = range(3332, 5684)
        #
        # nodes = list(nodes_desc) + list(nodes_asc)
        #
        # for node in nodes:
        #     url_full = str(url) + str(node) + '/'
        #     html = Text.api_get(self, url_full)
        #     filename, title, date, text = self.parse_html(html)
        #     if text:
        #         Text.write_txt_file(self, basefolder, filename, title, date, text)

        # Manually sort txt files by convocations. Then run code below
        #
        # 3rd convocation: 2000 - 2003
        # 4th convocation: 2004 - 2007
        # 5th convocation: 2008 - 2011
        # 6th convocation: 2012 - 2016
        # 7th convocation: 2017 - 2021

        confirm = False
        while confirm != 'y':
            print('Input "y" when you had sorted files\nReady? ')
            confirm = input()

        try:
            self.count(basefolder)
        except FileNotFoundError:
            print('FileNotFoundError')

        self.analyze(basefolder)
