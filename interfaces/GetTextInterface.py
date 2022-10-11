from abc import abstractmethod


class GetTextInterface:

    @abstractmethod
    def api_get(self, url) -> str:
        pass

    @abstractmethod
    def parse_html(self, html) -> str:
        pass

    @abstractmethod
    def write_txt_file(self, basefolder, filename, title, date, text):
        pass
