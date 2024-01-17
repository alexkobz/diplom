import asyncio
from texts.GosDuma import GosDuma
from texts.Izvestia import Izvestia
from texts.Kommersant import Kommersant
from texts.Vedomosti import Vedomosti
from texts.Echo import Echo
from texts.NG import NG
from texts.Zavtra import Zavtra
from texts.MK import MK
import const.const as const


async def main():

    izvestia = Izvestia(const.IZVESTIA.url, const.IZVESTIA.basefolder, const.IZVESTIA.timeout, const.IZVESTIA.pattern)
    kommersant = Kommersant(const.KOMMERSANT.url, const.KOMMERSANT.basefolder, const.KOMMERSANT.timeout, const.KOMMERSANT.pattern)
    vedomosti_politics = Vedomosti(const.VEDOMOSTI_POLITICS.url, const.VEDOMOSTI_POLITICS.basefolder, const.VEDOMOSTI_POLITICS.timeout, const.VEDOMOSTI_POLITICS.pattern)
    vedomosti_opinion = Vedomosti(const.VEDOMOSTI_OPINION.url, const.VEDOMOSTI_OPINION.basefolder, const.VEDOMOSTI_OPINION.timeout, const.VEDOMOSTI_OPINION.pattern)
    echo = Echo(const.ECHO.url, const.ECHO.basefolder, const.ECHO.timeout, const.ECHO.pattern)
    ng = NG(const.NG.url, const.NG.basefolder, const.NG.timeout, const.NG.pattern)
    zavtra = Zavtra(const.ZAVTRA.url, const.ZAVTRA.basefolder, const.ZAVTRA.timeout, const.ZAVTRA.pattern)
    mk = MK(const.MK.url, const.MK.basefolder, const.MK.timeout, const.MK.pattern)

    izvestia.save_urls()
    kommersant.save_urls()
    vedomosti_politics.save_urls()
    vedomosti_opinion.save_urls()
    echo.save_urls()
    ng.save_urls()
    zavtra.save_urls()
    mk.save_urls()

    izvestia_task = asyncio.create_task(izvestia())
    kommersant_task = asyncio.create_task(kommersant())
    vedomosti_task = asyncio.create_task(vedomosti_politics())
    ng_task = asyncio.create_task(ng())
    zavtra_task = asyncio.create_task(zavtra())
    mk_task = asyncio.create_task(mk())
    await izvestia_task
    await kommersant_task
    await vedomosti_task
    await ng_task
    await zavtra_task
    await mk_task


if __name__ == '__main__':
    asyncio.run(main())

