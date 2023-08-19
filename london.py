from capital_city import CapitalCity


# ConcreteProductB1
class London(CapitalCity):
    def get_population(self) -> int:
        return 8900000

    def list_top_attractions(self) -> []:
        return ["Tower Bridge", "Buckingham Palace", "Big Ben"]
