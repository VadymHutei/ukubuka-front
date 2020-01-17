from models import ProductCardModel
from views import ProductCardView


class ProductCardHandler():

    def __init__(self):
        self._model = ProductCardModel()

    def getProductCardPage(self, id_=None, alias=None):
        view = ProductCardView()
        return view.render()
