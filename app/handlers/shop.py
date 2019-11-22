import sys
sys.path.append('core')
from core import AbstractHandler
from views import ShopView

class ShopHandler(AbstractHandler):

    def __init__(self):
        self.view = ShopView()

    def getPage(self):
        return self.view.render()
