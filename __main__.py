#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
"""
Python file for scrapping texts:
speeches of presidents Putin and Medvedev (source - kremlin.ru),
transcripts of the State Duma, articles in Kommersant, Izvestia, Vedomosti, the Muscovite komsomolets,
the Independent newspaper, Zavtra, transcripts of Echo of Moscow

Analysis in .ipynb in texts/*
"""

__author__ = "Alexander Kobzar"
__contact__ = "alexanderkobzarrr@gmail.com"
__github__ = "alexkobz"
__maintainer__ = "developer"
__created__ = "2024-04-11"
__modified__ = "2024-04-14"
__status__ = "Production"
__version__ = "0.0.2"

import asyncio
from texts.president.President import President
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

    president_transcripts = President('http://www.kremlin.ru/events/president/transcripts/')
    president_news = President('http://www.kremlin.ru/events/president/news/')
    gosduma = GosDuma('http://transcript.duma.gov.ru/node/')
    izvestia = Izvestia("https://iz.ru/")
    kommersant = Kommersant("https://www.kommersant.ru/doc/")
    vedomosti_politics = Vedomosti("https://www.vedomosti.ru/politics/articles/")
    vedomosti_opinion = Vedomosti("https://www.vedomosti.ru/opinion/articles/")
    echo = Echo("https://echo.msk.ru/personalno/")
    ng = NG("https://ng.ru/politics/")
    zavtra = Zavtra("https://zavtra.ru/blogs/")
    mk = MK("https://www.mk.ru/politics/")

    president_transcripts.save_urls()
    president_news.save_urls()
    gosduma.save_urls()
    izvestia.save_urls()
    kommersant.save_urls()
    vedomosti_politics.save_urls()
    vedomosti_opinion.save_urls()
    echo.save_urls()
    ng.save_urls()
    zavtra.save_urls()
    mk.save_urls()

    president = president_transcripts or president_news
    vedomosti = vedomosti_politics or vedomosti_opinion

    president_task = asyncio.create_task(president())
    gosduma_task = asyncio.create_task(gosduma())
    izvestia_task = asyncio.create_task(izvestia())
    kommersant_task = asyncio.create_task(kommersant())
    vedomosti_task = asyncio.create_task(vedomosti())
    ng_task = asyncio.create_task(ng())
    zavtra_task = asyncio.create_task(zavtra())
    mk_task = asyncio.create_task(mk())

    await president_task
    await gosduma_task
    await izvestia_task
    await kommersant_task
    await vedomosti_task
    await ng_task
    await zavtra_task
    await mk_task

    with SQL() as sql:
        president.parse_html(sql)
        president.clean_text(sql)
        gosduma.parse_html(sql)
        gosduma.clean_text(sql)
        izvestia.parse_html(sql)
        izvestia.clean_text(sql)
        kommersant.parse_html(sql)
        kommersant.clean_text(sql)
        vedomosti_politics.parse_html(sql)
        vedomosti_politics.clean_text(sql)
        echo.parse_html(sql)
        echo.clean_text(sql)
        ng.parse_html(sql)
        ng.clean_text(sql)
        zavtra.parse_html(sql)
        zavtra.clean_text(sql)
        mk.parse_html(sql)
        mk.clean_text(sql)


if __name__ == '__main__':
    asyncio.run(main())
