#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
"""
Python file for scrapping texts:
speeches of presidents Putin and Medvedev (source - kremlin.ru),
transcripts of the State Duma, articles in Kommersant, Izvestia, Vedomosti,
the Independent newspaper, Vzglyad, Zavtra, transcripts of Echo of Moscow

Analysis in .ipynb in texts/*
"""

__author__ = "Alexander Kobzar"
__contact__ = "alexanderkobzarrr@gmail.com"
__github__ = "alexkobz"
__maintainer__ = "developer"
__created__ = "2024-04-11"
__modified__ = "2024-04-14"
__status__ = "Production"
__version__ = "0.0.3"

import asyncio
from texts.president.President import President
from texts.gosduma.GosDuma import GosDuma
from texts.izvestia.Izvestia import Izvestia
from texts.kommersant.Kommersant import Kommersant
from texts.vedomosti.Vedomosti import Vedomosti
from texts.echo.Echo import Echo
from texts.ng.NG import NG
from texts.zavtra.Zavtra import Zavtra
from texts.vzglyad.Vzglyad import Vzglyad
from sql.SQL import SQL


async def main():

    president = President('http://www.kremlin.ru/events/president/')
    gosduma = GosDuma('http://transcript.duma.gov.ru/node/')
    izvestia = Izvestia("https://iz.ru/")
    kommersant = Kommersant("https://www.kommersant.ru/doc/")
    vedomosti = Vedomosti("https://www.vedomosti.ru/")
    echo = Echo("https://echo.msk.ru/personalno/")
    ng = NG("https://ng.ru/politics/")
    zavtra = Zavtra("https://zavtra.ru/blogs/")
    vzglyad = Vzglyad("http://www.vz.ru/opinions/")

    president.save_urls()
    gosduma.save_urls()
    izvestia.save_urls()
    kommersant.save_urls()
    vedomosti.save_urls()
    echo.save_urls()
    ng.save_urls()
    zavtra.save_urls()
    vzglyad.save_urls()

    president_task = asyncio.create_task(president())
    gosduma_task = asyncio.create_task(gosduma())
    izvestia_task = asyncio.create_task(izvestia())
    kommersant_task = asyncio.create_task(kommersant())
    vedomosti_task = asyncio.create_task(vedomosti())
    ng_task = asyncio.create_task(ng())
    zavtra_task = asyncio.create_task(zavtra())
    vzglyad_task = asyncio.create_task(vzglyad())

    await president_task
    await gosduma_task
    await izvestia_task
    await kommersant_task
    await vedomosti_task
    await ng_task
    await zavtra_task
    await vzglyad_task

    with SQL() as sql:
        president.parse_html(sql)
        president.clean_text(sql)
        gosduma.parse_html(sql)
        gosduma.clean_text(sql)
        izvestia.parse_html(sql)
        izvestia.clean_text(sql)
        kommersant.parse_html(sql)
        kommersant.clean_text(sql)
        vedomosti.parse_html(sql)
        vedomosti.clean_text(sql)
        echo.parse_html(sql)
        echo.clean_text(sql)
        ng.parse_html(sql)
        ng.clean_text(sql)
        zavtra.parse_html(sql)
        zavtra.clean_text(sql)
        vzglyad.parse_html(sql)
        vzglyad.clean_text(sql)


if __name__ == '__main__':
    asyncio.run(main())
