from models import CatalogModel
from views import CatalogView


class CatalogHandler():

    def __init__(self):
        self._model = CatalogModel()

    def getCatalogPage(self, category=None):
        view = CatalogView()
        return view.render()
