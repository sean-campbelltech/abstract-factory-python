from country import Country
from england_factory import EnglandFactory
from international_provider import InternationalProvider
from spain_factory import SpainFactory


def main():
    country = Country.SPAIN
    factory = InternationalProvider.create(country)
    language = factory.create_language()
    capital_city = factory.create_capital()

    print(f"Country: {country.name}")
    print(f"Language: {language.__class__.__name__}")
    print(f"Greet: {language.greet()}")
    print(f"Capital: {capital_city.__class__.__name__}")
    print(f"Total Population: {capital_city.get_population():,}")
    print(f"Top Attractions: {capital_city.list_top_attractions()}")


if __name__ == "__main__":
    main()
