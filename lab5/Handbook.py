from lab5.PrintedEdition import PrintedEdition


class Handbook(PrintedEdition):

    def __init__(self, name, year, appointment, publishing_house):
        super().__init__(name, year, publishing_house)
        self.__appointent = appointment

    def get_appointment(self):
        return self.__appointent

    def __str__(self):
        return super().__str__() + f'\nНазначение: {self.__appointent}'