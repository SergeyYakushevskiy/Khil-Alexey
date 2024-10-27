# Печатное издание - суперкласс, от которого будут наследоваться другие классы
class PrintedEdition:


    # Функция инициализации нового печатного издания. Все свойства заданы через "__", чтобы сделать их приватными
    # таким образом, никто извне не сможет изменить данные, заданные на этапе создания
    def __init__(self, name, year, publishing_house):
        self.__publishing_house = publishing_house
        self.__year = year
        self.__name = name

    # Для каждого свойства был создан соответствующий геттер, чтобы можно было получить
    # свойства для дальнейшей с ним работы

    def get_publishing_house(self):
        return self.__publishing_house

    def get_year(self):
        return self.__year

    def get_name(self):
        return self.__name

    # стандартный метод конвертации печатного издания в строку был переделан, чтобы информация передавалась в удобном формате
    def __str__(self):
        return f'Название: {self.__name}\nГод: {self.__year}\nИздание: {self.__publishing_house}'