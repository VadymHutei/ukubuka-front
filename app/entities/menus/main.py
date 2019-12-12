from core import Menu
from core.connect import ContentService

class MainMenu(Menu):

    def __init__(self):
        self.cs = ContentService()
        data = self.cs.get('menus', id='2', active='y')
        self._items = data['items']
