from core import AbstractHandler, responces
from views import ErrorView
import config


class ErrorHandler(AbstractHandler):

    def __init__(self, code):
        self.code = code
        self.view = ErrorView()

    def getPage(self):
        page = str(self.code)
        return self.view.render(page=page)
