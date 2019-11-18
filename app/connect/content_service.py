import requests

import config
from core import AbstractConnect

class ContentService(AbstractConnect):

    def __init__(self):
        self.url = config.CONTENT_SERVICE['url']

    def get(self, entity, **params):
        response = requests.get(
            self.url + entity,
            params=params
        )
        return response.json()
