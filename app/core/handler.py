from abc import ABC, abstractmethod

class AbstractHandler(ABC):

    @abstractmethod
    def getPage(self):
        pass
