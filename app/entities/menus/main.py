from core import Menu
from connect import ContentService

class MainMenu(Menu):

    def __init__(self):
        self.cs = ContentService()
        data = self.cs.get('menu', active='y')
        print(data)
