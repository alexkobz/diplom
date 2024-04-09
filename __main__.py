import asyncio
from texts.gosduma.GosDuma import GosDuma
from texts.izvestia.Izvestia import Izvestia
from texts.kommersant.Kommersant import Kommersant
from texts.vedomosti.Vedomosti import Vedomosti
from texts.echo.Echo import Echo
from texts.ng.NG import NG
from texts.zavtra.Zavtra import Zavtra
from texts.mk.MK import MK
from sql.SQL import SQL


async def main():

    # izvestia = Izvestia("https://iz.ru/")
    # kommersant = Kommersant("https://www.kommersant.ru/doc/")
    # vedomosti_politics = Vedomosti("https://www.vedomosti.ru/politics/articles/")
    # vedomosti_opinion = Vedomosti("https://www.vedomosti.ru/opinion/articles/")
    # echo = Echo("https://echo.msk.ru/personalno/")
    # ng = NG("https://ng.ru/politics/")
    # zavtra = Zavtra("https://zavtra.ru/blogs/")
    # mk = MK("https://www.mk.ru/politics/")
    # gosduma = GosDuma('http://transcript.duma.gov.ru/node/')
    #
    # izvestia.save_urls()
    # kommersant.save_urls()
    # vedomosti_politics.save_urls()
    # vedomosti_opinion.save_urls()
    # echo.save_urls()
    # ng.save_urls()
    # zavtra.save_urls()
    # mk.save_urls()
    # gosduma.save_urls()
    #
    # izvestia_task = asyncio.create_task(izvestia())
    # kommersant_task = asyncio.create_task(kommersant())
    # vedomosti_task = asyncio.create_task(vedomosti_politics())
    # ng_task = asyncio.create_task(ng())
    # zavtra_task = asyncio.create_task(zavtra())
    # mk_task = asyncio.create_task(mk())
    # gosduma_task = asyncio.create_task(gosduma())
    #
    # await izvestia_task
    # await kommersant_task
    # await vedomosti_task
    # await ng_task
    # await zavtra_task
    # await mk_task
    # await gosduma_task

    with SQL() as sql:
        pass
        # gosduma.parse_html()

if __name__ == '__main__':
    asyncio.run(main())

