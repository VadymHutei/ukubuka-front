import sys
sys.path.append('core')
sys.path.append('modules/homepage')
from instance import Instance
from view import HomepageView
import config

class Homepage(Instance):

    def __init__(self):
        self.view = HomepageView()

    def getPage(self):
        return self.view.render()
