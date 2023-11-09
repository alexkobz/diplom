from dataclasses import dataclass


@dataclass
class MediaData:
    url: str
    basefolder: str
    timeout: int
    pattern: str

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2296 YaBrowser/23.9.0.2296 Yowser/2.5 Safari/537.36"
IZVESTIA = MediaData("https://iz.ru/", "izvestia", 60, "")
# IZVESTIA = MediaData("https://iz.ru/search?text=%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F&sort=0&type=2&prd=3&date_from=2000-01-01&date_to=2021-09-16", "izvestia", 60, "")
# IZVESTIA = MediaData("https://iz.ru/search?text=%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F&sort=0&type=5&prd=3&date_from=2000-01-01&date_to=2021-09-16", "izvestia", 60, "")
# IZVESTIA = MediaData("https://iz.ru/1222290/dmitrii-migunov/nalogovaia-polureforma-v-ssha-otmeniaiut-poslableniia-trampa", "izvestia", 60, "")
# IZVESTIA = MediaData("https://iz.ru/rubric/politika", "izvestia", 60, "")
# KOMMERSANT = MediaData("https://www.kommersant.ru/doc/", "kommersant", 15, "oc/\d*$")
VEDOMOSTI = MediaData("https://www.vedomosti.ru/politics/articles/", "vedomosti", 15, "")
# VEDOMOSTI = MediaData("https://www.vedomosti.ru/opinion/articles/", "vedomosti", 15, "")
ECHO = MediaData("https://echo.msk.ru/personalno/", "echo", 60, "")
NG = MediaData("https://ng.ru/politics/", "ng", 15, ".html$")
ZAVTRA = MediaData("https://zavtra.ru/blogs/", "zavtra", 60, "")
MK = MediaData("https://www.mk.ru/politics/", "mk", 60, "")
