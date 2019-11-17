from abc import ABC, abstractmethod
import config

class AbstractTemplate(ABC):

    @abstractmethod
    def getDir(self):
        pass

    @abstractmethod
    def getPath(self):
        pass
