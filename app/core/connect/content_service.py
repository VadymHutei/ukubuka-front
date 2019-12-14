import requests

import config
from core import AbstractConnect
from errors import NotFoundError

class ContentServiceError(Exception):
    pass

class ContentService(AbstractConnect):

    def __init__(self):
        self._url = config.CONTENT_SERVICE['url']
        self._timeout = (
            config.CONNECT_TIMEOUT,
            config.READ_TIMEOUT
        )
        self._headers = {
            'Accept': 'application/json',
            'language': config.CURRENT_LANGUAGE
        }

    def get(self, entity, **params):
        response = requests.get(
            self._url + entity,
            timeout = self._timeout,
            headers = self._headers,
            params=params
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 404:
            raise NotFoundError
        else:
            raise ContentServiceError
