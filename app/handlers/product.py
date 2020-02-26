from models import ProductModel
from views import ProductView


class ProductHandler():

    def __init__(self):
        self._model = ProductModel()
        self._view = ProductView()

    def getProductPage(self, path, alias=None, product_id=None):
        product = self._model.getProduct(alias, product_id)
        self._view.setParam('product', product)
        self._view.setLayout('beta/layout/layout.html')
        page = self._view.render()
        return page
