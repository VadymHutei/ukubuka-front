from flask import render_template

from core import AbstractView, Layout, Template


class ErrorView(AbstractView):

    def __init__(self):
        self.dir = 'error'
        self.params = {
            'layout': Layout(dir_='layout/error'),
        }

    def render(self, page='404'):
        template = Template(page, dir_=self.dir)
        return render_template(template.getPath(), **self.params)
