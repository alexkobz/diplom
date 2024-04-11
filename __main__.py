#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
"""
Python file for scrapping texts:
speeches of presidents Putin and Medvedev (source - kremlin.ru),
transcripts of the State Duma, articles in Kommersant, Izvestia, Vedomosti, the Muscovite komsomolets,
the Independent newspaper, Zavtra, transcripts of Echo of Moscow

Analysis in .ipynb in texts/*

Date created: 2024-04-11
"""

__author__ = "Alexander Kobzar"
__contact__ = "alexanderkobzarrr@gmail.com"
__date__ = "2024-04-11"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

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

    izvestia = Izvestia("https://iz.ru/")
    kommersant = Kommersant("https://www.kommersant.ru/doc/")
    vedomosti_politics = Vedomosti("https://www.vedomosti.ru/politics/articles/")
    vedomosti_opinion = Vedomosti("https://www.vedomosti.ru/opinion/articles/")
    echo = Echo("https://echo.msk.ru/personalno/")
    ng = NG("https://ng.ru/politics/")
    zavtra = Zavtra("https://zavtra.ru/blogs/")
    mk = MK("https://www.mk.ru/politics/")
    gosduma = GosDuma('http://transcript.duma.gov.ru/node/')

    izvestia.save_urls()
    kommersant.save_urls()
    vedomosti_politics.save_urls()
    vedomosti_opinion.save_urls()
    echo.save_urls()
    ng.save_urls()
    zavtra.save_urls()
    mk.save_urls()
    gosduma.save_urls()

    vedomosti = vedomosti_politics or vedomosti_opinion

    izvestia_task = asyncio.create_task(izvestia())
    kommersant_task = asyncio.create_task(kommersant())
    vedomosti_task = asyncio.create_task(vedomosti())
    ng_task = asyncio.create_task(ng())
    zavtra_task = asyncio.create_task(zavtra())
    mk_task = asyncio.create_task(mk())
    gosduma_task = asyncio.create_task(gosduma())

    await izvestia_task
    await kommersant_task
    await vedomosti_task
    await ng_task
    await zavtra_task
    await mk_task
    await gosduma_task

    with SQL() as sql:
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
