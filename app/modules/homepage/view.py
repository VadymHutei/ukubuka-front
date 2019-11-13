from flask import render_template
import config

class HomepageView():

    def __init__(self):
        # theme = config.CUR_THEME
        self.template = 'beta/homepage/homepage.html'
        self.params = {
            'layout': 'beta/layout/layout.html'
        }

    def render(self):
        return render_template(self.template, **self.params)
