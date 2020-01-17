from models import ShopModel
from views import ProductCardView


class ProductCardHandler():

    def __init__(self):
        self._model = ProductCardModel()

    def getProductCardPage(self):
        view = ProductCardView()
        return view.render()
