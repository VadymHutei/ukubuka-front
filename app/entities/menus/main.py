from core import Menu
from core.connect import ContentService

class MainMenu(Menu):

    def __init__(self):
        self.cs = ContentService()
        data = self.cs.get('menus', menu='main', active='y')
        self._items = self._createStructure(data)
