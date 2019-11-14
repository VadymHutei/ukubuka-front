import sys
sys.path.append('core')
from pathlib import Path, PurePath
from flask import render_template
from core import AbstractView
import config

class HomepageView(AbstractView):

    def __init__(self):
        self.theme = Path(config.SITE_THEME)
        self.params = {
            'layout': self._getLayout()
        }

    def _getLayout(self):
        layout_dir = self.theme / 'layout'
        layout_path = layout_dir / 'layout.html'
        layout_header_path = layout_dir / 'header.html'
        return {
            'dir': str(layout_dir),
            'path': str(layout_path),
            'header': str(layout_header_path)
        }

    def _getTemplate(self, template='homepage'):
        template_dir = self.theme / template
        template_path = template_dir / f'{template}.html'
        return {
            'dir': str(template_dir),
            'path': str(template_path),
        }

    def render(self):
        template = self._getTemplate()
        return render_template(template['path'], **self.params)
