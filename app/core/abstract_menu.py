from abc import ABC, abstractmethod
import config

class AbstractMenu(ABC):

    @abstractmethod
    def __iter__(self):
        pass