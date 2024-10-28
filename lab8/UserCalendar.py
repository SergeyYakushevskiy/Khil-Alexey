import calendar
import locale
from datetime import datetime


class UserCalendar:
    """Зададим константы. Словарь праздников, где ключ - месяц, значение - список праздничных дней"""
    holidays = {
        1:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        2:[23],
        3:[8],
        5:[1, 9],
        6:[12],
        11:[4]
    }
    """Кодировки цветов для разных типов дней"""
    day_color = '\033[0m'
    weekend_color = '\033[34m'
    holiday_color = '\033[1;31m'

    """Если год или месяц не числовые типы, и если они выходят за пределы допустимых значений, то выводится ошибка"""
    def __init__(self, year, month):
        if not isinstance(year, int):
            raise ValueError('Год является объектом типа int')
        if not isinstance(month, int):
            raise ValueError('Год является объектом типа int')
        if year < 0:
            raise ValueError('Год не может быть отрицательным')
        if month <= 0 or month > 12:
            raise ValueError('Месяц должен быть выбран в промежутке от 1 до 12')
        self.__year = year
        self.__month = month


    """Функции задания и получения данных о календаре: месяц, год и сам календарь"""
    @property
    def month_calendar(self):
        return calendar.monthcalendar(self.__year, self.__month)

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise ValueError('Год является объектом типа int')
        if year < 0:
            raise ValueError('Год не может быть отрицательным')
        self.__year = year

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise ValueError('Год является объектом типа int')
        if month <= 0 or month > 12:
            raise ValueError('Месяц должен быть выбран в промежутке от 1 до 12')
        self.__month = month


    """При выводе календаря в строку будет несколько этапов"""
    def __str__(self):
        """Задание страны - Россия"""
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        """Выравнивание месяца и года календаря по центру"""
        header_month = '{:^20}'.format(datetime(year=self.__year, month=self.__month, day=1).strftime('%B %Y'))
        """Задание заголовков для дней недели"""
        header_days = ' '.join(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])
        """Получение календаря"""
        month = calendar.monthcalendar(self.__year, self.__month)
        """Словарь цветов, где ключ - день месяца, значение - его цвет"""
        color_dict = {0 : ''}
        """Выполняем итерацию по всем значениям месяца и сопоставляем его с праздниками и выходными. Каждому дню присваиваем цвет и записываем в словарь цветов"""
        for week_i in range(len(month)):
            for day_i in range(len(month[0])):
                if month[week_i][day_i] in UserCalendar.holidays[self.__month]:
                    color_dict[month[week_i][day_i]] = UserCalendar.holiday_color
                elif day_i == 5 or day_i == 6:
                    color_dict[month[week_i][day_i]] = UserCalendar.weekend_color
                else:
                    color_dict[month[week_i][day_i]] = UserCalendar.day_color

        out = [header_month, header_days]
        """Добавляем каждому дню его цвет и записываем всё в выходную переменную"""
        for week in month:
            week_str = ' '.join(str(color_dict.get(j)) + "{:2}".format(j) for j in week).replace(' 0', '  ')
            out.append(week_str)
        return '\n'.join(out) # т.к. out - это список строк, то каждую строку списка будем выводить с новой строки \n