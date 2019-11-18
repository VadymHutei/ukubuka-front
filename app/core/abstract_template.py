from abc import ABC, abstractmethod

class AbstractTemplate(ABC):

    @abstractmethod
    def getDir(self):
        pass

    @abstractmethod
    def getPath(self):
        pass
