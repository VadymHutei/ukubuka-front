import sys
sys.path.append('modules/homepage')
from view import View

class Homepage():

    def __init__(self):
        self.view = View()
        print('Homepage created')

    def getPage(self):
        return self.view.render()
