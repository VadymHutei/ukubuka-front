from pathlib import Path

from flask import render_template


class View():

    _template = None
    _layout = None
    _params = {}

    def _setTemplate(self, template_path):
        self._template = Path(template_path)

    def setLayout(self, layout_path):
        self._layout = Path(layout_path)

    def setParam(self, name, value):
        self._params[name] = value

    def _render(self):
        return render_template(self._template, **self._params)

    def render(self):
        return self._render()