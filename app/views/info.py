from flask import render_template

from core import AbstractView, Layout, Template
from entities.menus import MainMenu


class InfoView(AbstractView):

    def __init__(self):
        self.params = {
            'layout': Layout(),
            'menu': MainMenu()
        }

    def render(self):
        return 'info'
        template = Template('info')
        return render_template(template.getPath(), **self.params)
