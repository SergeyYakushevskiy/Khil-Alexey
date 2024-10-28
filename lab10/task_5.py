import numpy as np

def print_matrix(matrix, cell_length=2): # функция для форматирования и вывода матрицы в консоль
    cell = '{:>' + str(cell_length) + '}'
    for row in matrix:
        print(*[cell.format(elem) for elem in row])

"""Ax=B"""
A = np.array([ #выписанные из системы уравнений кожффициенты при x_i
    [1, 2, 3],
    [2, 2, -2],
    [3, 1, 1]
])

print('\nМатрица коэффициентов\n')
print_matrix(A)

B = np.array([ #Свобоные коэффициенты перенесены в правую часть уравнений и записаны в виде вектор-столбца
    [-1],
    [4],
    [1],
])

print('\nМатрица свободных членов\n')
print_matrix(B)

x = np.linalg.solve(A, B) # функция решения СЛАУ
print('\nА*x = B')
print('x =')
print_matrix(x)
