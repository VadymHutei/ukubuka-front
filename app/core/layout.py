from core import AbstractLayout, Template

class Layout(AbstractLayout):

    def __init__(self, name='layout', dir_='layout'):
        self.dir = dir_
        self.template = Template(name, dir_)

    def getTemplate(self):
        return self.template

    def getComponent(self, name, dir_=None):
        if name not in dir(self):
            if dir_ is None:
                dir_ = self.dir
            self.header = Template(name, dir_)
        return self.header
