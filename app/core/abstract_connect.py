from abc import ABC, abstractmethod

class AbstractConnect(ABC):

    @abstractmethod
    def get(self, entity, **params):
        pass
