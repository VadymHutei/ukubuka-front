from models import ShopModel
from views import ShopView


class ShopHandler():

    def __init__(self):
        self._model = ShopModel()

    def getShopPage(self):
        view = ShopView()
        sections = self._model.getSections()
        view.setParam('sections', sections)
        return view.render()
