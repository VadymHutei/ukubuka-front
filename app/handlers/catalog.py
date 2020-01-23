from models import CatalogModel
from views import CatalogView


class CatalogHandler():

    def __init__(self):
        self._model = CatalogModel()
        self._view = CatalogView()

    def getCatalogPage(self, category=None):
        products = self._model.getCategoryProducts(category)
        self._view.setParam('products', products)
        page = self._view.render()
        return page
