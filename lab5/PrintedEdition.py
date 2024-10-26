class PrintedEdition:

    def __init__(self, publishing_house, year, name):
        self.__publishing_house = publishing_house
        self.__year = year
        self.__name = name

    def get_publishing_house(self):
        return self.__publishing_house
