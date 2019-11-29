from core import AbstractView, Layout
from entities.menus import MainMenu


class HomepageView(AbstractView):

    def __init__(self):
        self.setParam('layout', Layout())
        self.setParam('menu', MainMenu())

    def render(self):
        self._setTemplate('homepage')
        return self._render()
