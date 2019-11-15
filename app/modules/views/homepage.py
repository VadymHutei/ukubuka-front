from flask import render_template

from core import AbstractView, Layout, Template

class HomepageView(AbstractView):

    def __init__(self):
        self.params = {
            'layout': Layout()
        }

    def render(self):
        template = Template('homepage')
        return render_template(template.getPath(), **self.params)
