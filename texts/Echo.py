from texts.help.Media import Media
from time import sleep
from waybackpy import WaybackMachineCDXServerAPI
import const.const as const


class Echo(Media):

    user_agent = const.USER_AGENT

    async def __call__(self) -> None:
        self.mkdir()
        known_urls = self.get_known_urls()

        file_count = 1
        for url in known_urls:
            save_api = WaybackMachineCDXServerAPI(url, user_agent=Echo.user_agent)
            archive_url = save_api.newest().archive_url
            try:
                self.get_pages(archive_url, file_count)
                file_count += 1
                sleep(0.1)
            except:
                sleep(self._timeout + 1)