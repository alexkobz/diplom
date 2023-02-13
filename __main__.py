from GosDuma import GosDuma
from Media import *


def main():
    gd = GosDuma()
    gd.api_get()

    izvestia = Izvestia()
    izvestia._api_get()


if __name__ == '__main__':
    main()


