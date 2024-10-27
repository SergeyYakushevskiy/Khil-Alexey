from multiprocessing.dummy import Value


class UserComplex:

    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary

    @property
    def real(self):
        return self.__real

    @property
    def imaginary(self):
        return self.__imaginary

    @real.setter
    def real(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Вещественная часть не может быть типом {}'.format(type(value)))
        self.__real = value

    @imaginary.setter
    def imaginary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Вещественная часть не может быть типом {}'.format(type(value)))
        self.__imaginary = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            real = self.real + other
            return self.__class__(real, self.__imaginary)
        elif isinstance(other, UserComplex):
            real = self.real + other.real
            imag = self.imaginary + other.imaginary
            return self.__class__(real, imag)
        else:
            raise ValueError('Сложение с типом данных {} не поддерживается'.format(type(other)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            real = self.real * other
            imag = self.imaginary * other
            return self.__class__(real, imag)
        elif isinstance(other, UserComplex):
            real = self.real * other.imaginary - self.imaginary * other.imaginary
            imag = self.imaginary * other.real - self.real * other.imaginary
            return self.__class__(real, imag)
        else:
            raise ValueError('Умножение с типом данных {} не поддерживается'.format(type(other)))

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            real = self.real - other
            return self.__class__(real, self.__imaginary)
        elif isinstance(other, UserComplex):
            real = self.real - other.real
            imag = self.imaginary - other.imaginary
            return self.__class__(real, imag)
        else:
            raise ValueError('Сложение с типом данных {} не поддерживается'.format(type(other)))

    def __repr__(self):
        real = str(self.real) if self.real != 0 else ''
        imag = str(self.imaginary) + 'j' if self.imaginary != 0 else ''
        return  real + imag

    def __eq__(self, other):
        """ Функция сравнения двух комплексных чисел. """
        return isinstance(other, UserComplex) and all(getattr(self, attr) == getattr(other, attr) for attr in vars(self))