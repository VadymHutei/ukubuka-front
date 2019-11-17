from abc import ABC, abstractmethod
import config

class AbstractLayout(ABC):

    @abstractmethod
    def getTemplate(self):
        pass

    @abstractmethod
    def getComponent(self):
        pass
