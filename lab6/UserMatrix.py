import copy

class UserMatrix:



    def __init__(self, matrix):
        """Если полученный объект не является списком, или же все его элементы не равные списки, то матрица не создаётся"""
        if not isinstance(matrix, list):
            raise ValueError('Матрица должна быть типа list')
        matrix_len = len(matrix[0])
        for elem in matrix:
            if not isinstance(matrix, list):
                raise ValueError('Строки матрицы должны быть типа list')
            if matrix_len != len(elem):
                raise ValueError('Все строки матрицы должны быть одной длины')
        self.__matrix = matrix

    @property
    def matrix(self):
        """Возвращаем копию матрицы, чтобы при работе случайно не изменить исходную"""
        return copy.deepcopy(self.matrix)


    @matrix.setter
    def matrix(self, matrix):
        """Задать новую матрицу можно только по условиям, описанным в конструкторе"""
        if not isinstance(matrix, list):
            raise ValueError('Матрица должна быть типа list')
        matrix_len = len(matrix[0])
        for elem in matrix:
            if not isinstance(matrix, list):
                raise ValueError('Строки матрицы должны быть типа list')
            if matrix_len != len(elem):
                raise ValueError('Все строки матрицы должны быть одной длины')
        self.__matrix = matrix


    """Получение длины и ширины матрицы"""
    @property
    def width(self):

        return len(self.__matrix[0])

    @property
    def height(self):
        return len(self.__matrix)


    def __add__(self, other):
        """Складывать и вычитать можно только матрицы с одинаковыми размерами"""
        if not isinstance(other, UserMatrix):
            raise ValueError('Нельзя сложить матрицу с объектом типа {}'.format(type(other)))
        if self.width != other.width or self.height != other.height:
            raise ValueError('Матрицы не равны по размерам')
        matrix = copy.deepcopy(self.matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += other.matrix[i][j]
        return self.__class__(matrix)

    def __sub__(self, other):
        if not isinstance(other, UserMatrix):
            raise ValueError('Нельзя вычесть из матрицы объект типа {}'.format(type(other)))
        if self.width != other.width or self.height != other.height:
            raise ValueError('Матрицы не равны по размерам')
        matrix = copy.deepcopy(self.matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] -= other.matrix[i][j]
        return self.__class__(matrix)

    def __mul__(self, other):
        """A[m x n] * B [n x k] = C [m x k]"""
        if isinstance(other, (int, float)):
            matrix = copy.deepcopy(self.matrix)
            matrix = [[matrix[row][column] * other for column in row]for row in matrix]
            return self.__class__(matrix)
        if isinstance(other, UserMatrix):
            if self.width != other.height:
                raise ValueError('Матрицы не равны по размерам')
            matrix = [[sum(a * b for a, b in zip(row, column)) for column in zip(*self.matrix)] for row in self.matrix]
            return self.__class__(matrix)
        raise ValueError('Нельзя умножить матрицу на объект типа {}'.format(type(other)))


    def __str__(self):
        string = '\n'
        for row in self.__matrix:
            string += '[' + ' '.join([str(i) for i in row]) + ']\n'
        return string

    def __eq__(self, other):
        """ Функция сравнения двух матриц. """
        return isinstance(other, UserMatrix) and all(getattr(self, attr) == getattr(other, attr) for attr in vars(self))