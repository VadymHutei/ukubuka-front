from models import ShopModel
from views import ShopView


class ShopHandler():

    def __init__(self):
        self._model = ShopModel()
        self._view = ShopView()

    def getShopPage(self):
        sections = self._model.getSections()
        self._view.setLayout('beta/layout/layout.html')
        self._view.setParam('sections', sections)
        page = self._view.render()
        return page
