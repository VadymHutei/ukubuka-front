from abc import ABC, abstractmethod

class Instance(ABC):

    @abstractmethod
    def getPage(self):
        pass