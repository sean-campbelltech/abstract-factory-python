from abc import ABC, abstractmethod


# AbstractProductA
class Language(ABC):
    @abstractmethod
    def greet(self) -> str:
        pass
