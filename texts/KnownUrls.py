#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import waybackpy
from const.const import USER_AGENT


class KnownUrls:

    def __init__(self, url):
        self.url = url

    def get_urls(self):
        return waybackpy.Url(url=self.url, user_agent=USER_AGENT).known_urls(subdomain=False)  # alive and subdomain are optional.
