from lab5.PrintedEdition import PrintedEdition


# Унаследован от печатного издания. Добавлены свойства номера выпуска и месяц.
# Конвертация в строку вызывает строку печатного издания с добавлением номера издания и месяца
class Journal(PrintedEdition):

    def __init__(self, name, number, month,
                 year, publishing_house):
        super().__init__(name, year, publishing_house)
        self.__number = number
        self.__month = month

    def get_number(self):
        return self.__number

    def get_month(self):
        return self.__month

    def __str__(self):
        return super().__str__() + f'\nНомер: {self.__number}\nМесяц: {self.__month}'

