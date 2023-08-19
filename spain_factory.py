from capital_city import CapitalCity
from international_factory import InternationalFactory
from language import Language
from madrid import Madrid
from spanish import Spanish


# ConcreteFactory2
class SpainFactory(InternationalFactory):
    def create_language(self) -> Language:
        return Spanish()

    def create_capital(self) -> CapitalCity:
        return Madrid()
