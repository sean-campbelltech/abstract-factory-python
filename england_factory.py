from capital_city import CapitalCity
from english import English
from international_factory import InternationalFactory
from language import Language
from london import London


# ConcreteFactory1
class EnglandFactory(InternationalFactory):
    def create_language(self) -> Language:
        return English()

    def create_capital(self) -> CapitalCity:
        return London()
