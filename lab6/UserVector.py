class UserVector:

    def __init__(self, *args):
        if len(args) == 0:
            self.__values = (0, 0)
        else:
            self.__values = args

    def __add__(self, other):
        """ Возвращает векторное сложение себя и другого вектора"""
        if isinstance(other, UserVector):
            added = tuple(a + b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            added = tuple(a + other for a in self)
        else:
            raise ValueError("Добавление с типом {} не поддерживается".format(type(other)))
        return self.__class__(*added)

    def inner(self, vector):
        """ Возвращает точечное произведение (внутреннее произведение) себя и другого вектора """
        if not isinstance(vector, UserVector):
            raise ValueError('Для точечного произведения нужен другой вектор')
        return sum(a * b for a, b in zip(self, vector))

    def __mul__(self, other):
        """ Возвращает скалярное произведение себя и другого, если умножается на другой вектор."""
        if isinstance(other, UserVector):
            return self.inner(other)
        elif isinstance(other, (int, float)):
            product = tuple(a * other for a in self)
            return self.__class__(*product)
        else:
            raise ValueError("Умножение с типом {} не поддерживается".format(type(other)))

    def __sub__(self, other):
        """ Возвращает результат вычитания векторов """
        if isinstance(other, UserVector):
            subbed = tuple(a - b for a, b in zip(self, other))
        elif isinstance(other, (int, float)):
            subbed = tuple(a - other for a in self)
        else:
            raise ValueError("Умножение с типом данных {} не поддерживается".format(type(other)))
        return self.__class__(*subbed)


    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, *args):
        if len(args) == 0:
            self.__values = (0, 0)
        else:
            self.__values = args

    def __iter__(self):
        """Даёт возможность выполнять итерации по значениям вектора"""
        return self.values.__iter__()

    def __len__(self):
        """ Переопределение длины вектора"""
        return len(self.values)

    def __getitem__(self, key):
        """ Получение значения вектора по ключу. Нумерация с 0"""
        return self.values[key]

    def __repr__(self):
        """ Нужен для официального текстового представления вектора"""
        return str(self.values)

    def __eq__(self, other):
        """ Функция сравнения двух векторов. """
        return isinstance(other, UserVector) and all(getattr(self, attr) == getattr(other, attr) for attr in vars(self))