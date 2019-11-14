import sys
sys.path.append('core')
from pathlib import Path, PurePath
from flask import render_template
from core import AbstractView
import config

class HomepageView(AbstractView):

    def __init__(self):
        self.theme = Path(config.SITE_THEME)
        self.layout_dir = self.theme / 'layout'
        self.layout = self.layout_dir / 'layout.html'
        self.template_dir = self.theme / 'homepage'
        self.template = self.template_dir / 'homepage.html'
        self.params = {
            'layout': str(self.layout)
        }

    def render(self):
        template = str(self.template)
        params = self.params
        return render_template(template, **params)
