from capital_city import CapitalCity


# ConcreteProductB2
class Madrid(CapitalCity):
    def get_population(self) -> int:
        return 3200000

    def list_top_attractions(self) -> []:
        return ["Royal Palace", "Prado Museum", "Retiro Park"]
