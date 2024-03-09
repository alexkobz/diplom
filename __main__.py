import asyncio
from texts.GosDuma import GosDuma
from texts.Izvestia import Izvestia
from texts.Kommersant import Kommersant
from texts.Vedomosti import Vedomosti
from texts.Echo import Echo
from texts.NG import NG
from texts.Zavtra import Zavtra
from texts.MK import MK


async def main():

    izvestia = Izvestia("https://iz.ru/")
    kommersant = Kommersant("https://www.kommersant.ru/doc/")
    vedomosti_politics = Vedomosti("https://www.vedomosti.ru/politics/articles/")
    vedomosti_opinion = Vedomosti("https://www.vedomosti.ru/opinion/articles/")
    echo = Echo("https://echo.msk.ru/personalno/")
    ng = NG("https://ng.ru/politics/")
    zavtra = Zavtra("https://zavtra.ru/blogs/")
    mk = MK("https://www.mk.ru/politics/")
    gosduma = GosDuma()
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

