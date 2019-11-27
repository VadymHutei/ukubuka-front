from core import AbstractView, Layout
from entities.menus import MainMenu


class CatalogView(AbstractView):

    def __init__(self):
        self._setParam('layout', Layout())
        self._setParam('menu', MainMenu())

    def render(self):
        self._setTemplate('shop/catalog')
        return self._render()
