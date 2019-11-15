from pathlib import Path

import config

class Template():

    def __init__(self, name, dir_=None):
        self.theme = Path(config.SITE_THEME)
        self.name = name
        self.dir = self.theme / (dir_ if dir_ is not None else name)
        self.path = self.dir / f'{name}.html'

    def getDir(self):
        return str(self.dir)

    def getPath(self):
        return str(self.path)
