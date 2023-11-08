from threading import Thread
from texts.GosDuma import GosDuma
from texts.Izvestia import Izvestia
from texts.Kommersant import Kommersant
from texts.Vedomosti import Vedomosti
from texts.Echo import Echo
from texts.NG import NG
from texts.Zavtra import Zavtra
from texts.MK import MK
import const.const as const


def main():
    izvestia = Izvestia(const.IZVESTIA.url, const.USER_AGENT, const.IZVESTIA.basefolder, const.IZVESTIA.timeout)
    kommersant = Kommersant(const.KOMMERSANT.url, const.USER_AGENT, const.KOMMERSANT.basefolder, const.KOMMERSANT.timeout)
    vedomosti = Vedomosti(const.VEDOMOSTI.url, const.USER_AGENT, const.VEDOMOSTI.basefolder, const.VEDOMOSTI.timeout)
    echo = Echo(const.ECHO.url, const.USER_AGENT, const.ECHO.basefolder, const.ECHO.timeout)
    ng = NG(const.NG.url, const.USER_AGENT, const.NG.basefolder, const.NG.timeout)
    zavtra = Zavtra(const.ZAVTRA.url, const.USER_AGENT, const.ZAVTRA.basefolder, const.ZAVTRA.timeout)
    mk = MK(const.MK.url, const.USER_AGENT, const.MK.basefolder, const.MK.timeout)

    # echo_thread = Thread(target=echo(), args=(echo.get_known_urls(), echo.basefolder,))
    # echo_thread.start()
    # echo_thread.join()


if __name__ == '__main__':
    main()



