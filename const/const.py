from dataclasses import dataclass


@dataclass
class MediaData:
    url: str
    basefolder: str
    timeout: int
    pattern: str


BASEFOLDER = f'D:\diplom main'
USER_AGENT = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/116.0.5845.2296 YaBrowser/23.9.0.2296 Yowser/2.5 Safari/537.36"}

IZVESTIA = MediaData("https://iz.ru/", "izvestia", 60, "iz.ru/\d+/[^\d]+/[\w-]*$")
KOMMERSANT = MediaData("https://www.kommersant.ru/doc/", "kommersant", 15, "oc/\d*$")
VEDOMOSTI_POLITICS = MediaData("https://www.vedomosti.ru/politics/articles/", "vedomosti", 15,
                               "politics/articles/\d{4}/\d{2}/\d{2}/[\w-]*$")
VEDOMOSTI_OPINION = MediaData("https://www.vedomosti.ru/opinion/articles/", "vedomosti", 15,
                              "opinion/articles/\d{4}/\d{2}/\d{2}/[\w-]*$")
ECHO = MediaData("https://echo.msk.ru/personalno/", "echo", 60, "")
NG = MediaData("https://ng.ru/politics/", "ng", 15, ".html$")
ZAVTRA = MediaData("https://zavtra.ru/blogs/", "zavtra", 60, "")
MK = MediaData("https://www.mk.ru/politics/", "mk", 60, ".html$")
