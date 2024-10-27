from lab6.UserComplex import UserComplex
from lab6.UserMatrix import UserMatrix
from lab6.UserVector import UserVector

"""Создаём три разных вектора"""
vector_1 = UserVector(1, 2, 3, 4)
vector_2 = UserVector(4, 3, 2, 1)
vector_3 = UserVector(4, 3, 2, 1)


"""Вывод на экран созданных векторов и демонстрация всех оперций над векторами"""
print('vector_1:', vector_1)
print('vector_2:', vector_2)
print('vector_3:', vector_3)
print('vector_1 + vector_2=', vector_1 + vector_2)
print('vector_1 - vector_2=',vector_1 - vector_2)
print('vector_1 * vector_2=', vector_1 * vector_2)
print('vector_1 == vector_2:', vector_1 == vector_2)
print('vector_2 == vector_3:', vector_2 == vector_3)

print()
"""Создаём 3 комплексных числа"""
complex_1 = UserComplex(4, 5)
complex_2 = UserComplex(-3, 5)
complex_3 = UserComplex(-3, 5)
"""Вывод всех операций"""
print('complex_1:', complex_1)
print('complex_2:', complex_2)
print('complex_3:', complex_3)
print('complex_1 + complex_2 =', complex_1 + complex_2)
print('complex_1 + 4.0 =', complex_1 + 4.0)
print('complex_1 - complex_2 =', complex_1 - complex_2)
print('complex_1 * complex_2 =', complex_1 * complex_2)
print('complex_1 == complex_2: ', complex_1 == complex_2)
print('complex_2 == complex_3: ', complex_2 == complex_3)


"""Создание трёх двумерных списков и создание на их основе трёх матриц"""
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_1 = UserMatrix(matrix_1)

matrix_2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


matrix_2 = UserMatrix(matrix_2)

matrix_3 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


matrix_3 = UserMatrix(matrix_3)


"""Вывод всех операций над матрицами"""
print('matrix_1:', matrix_1)
print('matrix_2:', matrix_2)
print('matrix_3:', matrix_3)
print('matrix_1 + matrix_2 =', matrix_1 + matrix_2)
print('matrix_2 - matrix_3 =', matrix_1 - matrix_2)
print('matrix_1 * matrix_2 =', matrix_1 * matrix_2)
print('matrix_1 == matrix_2:', matrix_1 == matrix_2)
print('matrix_2 == matrix_3:', matrix_2 == matrix_3)