from core import AbstractView, Layout
from entities.menus import MainMenu


class ProductCardView(AbstractView):

    def __init__(self):
        self.setParam('layout', Layout())
        self.setParam('menu', MainMenu())

    def render(self):
        self._setTemplate('shop/product_card')
        return self._render()
