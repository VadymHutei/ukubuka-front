from models import ShopModel
from views import ShopView, CatalogView, ProductCardView


class ShopHandler():

    def __init__(self):
        self._model = ShopModel()

    def getShopPage(self):
        view = ShopView()
        sections = self._model.getSections()
        view.setParam('sections', sections)
        return view.render()

    def getCatalogPage(self, category):
        view = CatalogView()
        return view.render()

    def getProductCardPage(self, id_):
        view = ProductCardView()
        return view.render()
