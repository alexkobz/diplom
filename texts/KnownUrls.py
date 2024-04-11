#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import waybackpy
import const.const as const


class KnownUrls:

    user_agent = const.USER_AGENT

    def __init__(self, url):
        self.url = url

    def get_urls(self):
        return waybackpy.Url(url=self.url, user_agent=KnownUrls.user_agent).known_urls(subdomain=False)  # alive and subdomain are optional.
