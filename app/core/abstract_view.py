from abc import ABC, abstractmethod

from flask import render_template

from core import Template

class AbstractView(ABC):

    _params = {}

    @abstractmethod
    def render(self):
        pass

    def _setTemplate(self, template):
        self.template = Template(template)

    def _render(self):
        return render_template(self.template.getPath(), **self._params)

    def setParam(self, name, value):
        self._params[name] = value
