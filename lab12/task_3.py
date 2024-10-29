import numpy as np
from matplotlib import pyplot as pl

x = np.linspace(-4, 4, 10)  # задаём отрезок нахождения решения диф. ура
y = x # область значений функции
X, Y = np.meshgrid(x, y) # вычисляем сетку значений

# задаём систему уравнений, эквивалентную диф. уравнению
DX = Y
DY = -X * Y - X

# строим фазовый портрет системы
pl.quiver(X, Y, DX, DY, color='k')
pl.xlabel('x')
pl.ylabel('y')
pl.show()
