import sys
sys.path.append('core')
from core import AbstractHandler
from modules.views import ShopView

class Shop(AbstractHandler):

    def __init__(self):
        self.view = ShopView()

    def getPage(self):
        return self.view.render()
