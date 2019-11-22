from core import AbstractHandler
from views import HomepageView

class HomepageHandler(AbstractHandler):

    def __init__(self):
        self.view = HomepageView()

    def getPage(self):
        return self.view.render()
