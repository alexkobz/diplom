import os
from Text import Text


class StateDuma(Text):

    def parse_html(self, html) -> (str, str, str, str):
        header = html.body.find('div', attrs={'class': 'header-bord'}).text.replace('\n', ' ')
        header_list = header.split()
        header_list = header_list[2:-4]
        header_list = header_list[:3]
        if header_list[0] == 'Стенограмма':
            title = ' '.join(header_list)
            transcript = html.body.find('div', attrs={'id': 'selectable-content'}).text
            return f'{title}.txt', title, title, transcript

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
