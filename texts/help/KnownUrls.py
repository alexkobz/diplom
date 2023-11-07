import waybackpy


class KnownUrls:

    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent
    
    def get_urls(self):
        return waybackpy.Url(url=self.url, user_agent=self.user_agent).known_urls(subdomain=False)  # alive and subdomain are optional.
