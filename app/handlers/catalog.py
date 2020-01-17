from models import ShopModel
from views import CatalogView


class CatalogHandler():

    def __init__(self):
        self._model = CatalogModel()

    def getCatalogPage(self):
        view = CatalogView()
        return view.render()
