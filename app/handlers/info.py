from core import AbstractHandler, responces
from views import InfoView

class InfoHandler(AbstractHandler):

    def __init__(self, page):
        self.page = page
        self.view = InfoView()

    def getPage(self):
        return False, responces.NOT_FOUND
