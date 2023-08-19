from abc import ABC, abstractmethod
from capital_city import CapitalCity
from language import Language


# AbstractFactory
class InternationalFactory(ABC):
    @abstractmethod
    def create_language(self) -> Language:
        pass

    @abstractmethod
    def create_capital(self) -> CapitalCity:
        pass
