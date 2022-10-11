import os
from classes.StateDuma import StateDuma


def main():

    __BASEFOLDER = r'C:\Users\kobzaale\Desktop\diplom'
    # __BASEFOLDER = os.getcwd()

    sd = StateDuma(__BASEFOLDER, 'http://transcript.duma.gov.ru/node/')
    sd(sd.basefolder, sd.url)


if __name__ == '__main__':
    main()
