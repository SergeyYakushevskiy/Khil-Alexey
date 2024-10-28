import numpy as np

def print_matrix(matrix, cell_length=2): # функция для форматирования и вывода матрицы в консоль
    cell = '{:>' + str(cell_length) + '}'
    for row in matrix:
        print(*[cell.format(elem) for elem in row])

A = np.array([ # создание матрицы как объекта класса np.array
    [2, 10, 4],
    [-3, 4, 22],
    [22, -8, 10]
])

B = np.array([
    [-2, 5, -6],
    [4, 10, 2],
    [6, 3, 3]
])

print('A =')
print_matrix(A)
print()

print('B =')
print_matrix(B)
print()

C = A + B
print('C = A + B = ')
print_matrix(C)
print()

C = A - B
print('C = A - B = ')
print_matrix(C)
print()

C = A * B
print('C = A * B = ')
print_matrix(C)
print()

print('Aᵀ =')
print_matrix(A.transpose())
print()

print('B⁻¹ =')
print_matrix(np.linalg.inv(B),cell_length= 20)
print()

print('determinant(A) =', np.linalg.det(A))