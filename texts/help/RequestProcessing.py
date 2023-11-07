from requests import get
from enum import Enum


class RequestResult(Enum):
    OK = '2'
    WRONG = '3'
    NOT_FOUND = '4'


class RequestProcessing:

    def __init__(self, url, user_agent, path, file_count):
        self._url = url
        self._user_agent = user_agent
        self._path = path
        self._file_count = file_count

    @property
    def user_agent(self):
        return self._user_agent

    def get(self):
        response = get(self._url)  # except
        if str(response.status_code)[0] != RequestResult.OK.value:
            return None
        return response

    def write(self, response):
        try:
            with open(f'{self._path}/{self._file_count}.html', 'wb+') as f:
                f.write(response.content)
        except Exception as e:
            with open(f'{self._path}/err.txt', 'a+') as f:
                f.write(response.txt)
                f.write('\n\n\n')

    def __call__(self, *args, **kwargs):
        response = self.get()
        if response:
            self.write(response)
