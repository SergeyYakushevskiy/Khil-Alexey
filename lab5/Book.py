from lab5.PrintedEdition import PrintedEdition


class Book(PrintedEdition):

    def __init__(self, name, topic, author, page_count, year, publishing_house):
        super().__init__(name, year, publishing_house)
        self.__topic = topic
        self.__author = author
        self.__page_count = page_count

    def get_topic(self):
        return self.__topic

    def get_author(self):
        return self.__author

    def get_page_count(self):
        return self.__page_count

    def __str__(self):
        return super().__str__() + (f'\nАвтор: {self.__author}'
                                    f'\nЖанр: {self.__topic}\nКоличество страниц: {self.__page_count}')
