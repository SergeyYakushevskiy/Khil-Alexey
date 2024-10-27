from lab5.Book import Book
from lab5.Handbook import Handbook
from lab5.Journal import Journal
from lab5.PrintedEdition import PrintedEdition

# Для демонстрации работы программы была создана универсальная функция,
# которая выводит информацию о печатном издании

def print_edition(some_edition):
    print(some_edition)
    print()


# создаётся 4 вида печатного издания, которые затем передаются в функцию для вывода на экран информации о них
printed_edition = PrintedEdition('Печатное издание', 1978, 'ДГТУ')
journal = Journal('Журнал', 3, 'May', 2024, 'ДГТУ')
book = Book('Горе от ума', 'Комедия', 'Александр Сергеевич Грибоедов', 352, 1824, 'Москва')
handbook = Handbook('Высшая математика', '2019', 'Для вузов', 'Хиль Алексей')

for edition in [printed_edition, journal, book, handbook]:
    print_edition(edition)