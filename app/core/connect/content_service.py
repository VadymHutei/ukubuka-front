import requests

import config
from core import AbstractConnect

class ContentServiceError(Exception):
    pass

class ContentService(AbstractConnect):

    def __init__(self):
        self.url = config.CONTENT_SERVICE['url']

    def get(self, entity, **params):
        try:
            response = requests.get(
                self.url + entity,
                params=params,
                timeout = (config.CONNECT_TIMEOUT, config.READ_TIMEOUT),
                headers = {
                    'Accept': 'application/json'
                }
            )
        except (requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.RequestException) as e:
            if config.MODE == 'dev':
                raise e
            else:
                return False
        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(response.status_code)
                raise ContentServiceError
