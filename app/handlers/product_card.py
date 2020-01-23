from models import ProductCardModel
from views import ProductCardView
from errors import HandlerError


class ProductCardHandler():

    def __init__(self):
        self._model = ProductCardModel()
        self._view = ProductCardView()

    def getProductCardPage(self, id_=None, alias=None):
        if id_ is not None:
            product = self._model.getProductByID(id_)
        elif alias is not None:
            product = self._model.getProductByAlial(alias)
        else:
            raise HandlerError('There aro no product ID or alias in params')
        self._view.setParam('product', product)
        page = self._view.render()
        return page
