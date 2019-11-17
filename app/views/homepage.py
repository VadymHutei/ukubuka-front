from flask import render_template

from core import AbstractView, Layout, Template
from entities.menus import MainMenu


class HomepageView(AbstractView):

    def __init__(self):
        self.params = {
            'layout': Layout(),
            'menu': MainMenu()
        }

    def render(self):
        template = Template('homepage')
        return render_template(template.getPath(), **self.params)
