from country import Country
from england_factory import EnglandFactory
from international_factory import InternationalFactory
from spain_factory import SpainFactory


class InternationalProvider:
    @staticmethod
    def create(country: Country) -> InternationalFactory:
        if country is Country.ENGLAND:
            return EnglandFactory()
        elif country is Country.SPAIN:
            return SpainFactory()
        else:
            raise ValueError(f"{country} is not currently supported.")
