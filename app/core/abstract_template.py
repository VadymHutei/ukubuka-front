from abc import ABC, abstractmethod
import config

class AbstractTemplate(ABC):

    def __init__(self, name):
        self.theme = Path(config.SITE_THEME)
        self.name = name

    @abstractmethod
    def setPath(self):
        pass

    @abstractmethod
    def getPath(self):
        pass
