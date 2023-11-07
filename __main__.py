# from texts.GosDuma import GosDuma
# from texts.Echo import Echo
# from texts.Izvestia import Izvestia
# from texts.Nezavisimaya import Nezavisimaya
#
#
# def main():
#     # gd = GosDuma()
#     # gd()
#
#     # echo = Echo()
#     # echo()
#
#     # izvestia = Izvestia()
#     # izvestia()
#     nezavisimaya = Nezavisimaya()
#     nezavisimaya()
#     pass
#
#
#
# if __name__ == '__main__':
#     main()
#
#
import asyncio
from requests import get
from threading import Thread
def foo(urls, basefolder):
    c = 0
    for url in urls:
        res = get(url)
        with open(f'{basefolder}/{c}.html', 'wb+') as f:
            f.write(res.content)
        c += 1
t1 = Thread(target=foo, args=(['https://zavtra.ru/blogs/1997-03-182few', 'https://zavtra.ru/blogs/2000-02-1533'],'zavtra',))
t2 = Thread(target=foo, args=(['http://www.ng.ru:80/politics/1999-10-05/education.html', 'https://www.ng.ru/politics/%201999-12-30/4_millenium.html'],'ng',))
t1.start()
t2.start()
t1.join()
t2.join()


