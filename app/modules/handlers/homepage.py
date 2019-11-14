import sys
sys.path.append('core')
from core import AbstractHandler
from modules.views import HomepageView

class Homepage(AbstractHandler):

    def __init__(self):
        self.view = HomepageView()

    def getPage(self):
        return self.view.render()
