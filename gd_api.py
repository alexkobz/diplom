import requests
from bs4 import BeautifulSoup


def api(nodes):
    path = r'C:\Users\kobzaale\Desktop\diplom'
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


def main():
    # 18 января 2000 г. - 22 октября 2010 г.
    nodes_reverse = range(2265, 43, -1)

    # 01 ноября 2010 г. - 17 июня 2021 г.
    nodes = range(3332, 3341)

    try:
        api(nodes_reverse)
        api(nodes)
    except ConnectionError:
        print('ConnectionError')
    except AttributeError:
        print('AttributeError')


if __name__ == '__main__':
    main()
