from core import AbstractView, Layout
from entities.menus import MainMenu


class ShopView(AbstractView):

    def __init__(self):
        self.setParam('layout', Layout())
        self.setParam('menu', MainMenu())
        self._setTemplate('shop')

    def render(self):
        return self._render()
