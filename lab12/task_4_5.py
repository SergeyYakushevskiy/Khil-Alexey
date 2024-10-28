import math
from matplotlib import pyplot as pl
import numpy as np
from numpy.ma.core import transpose

z = lambda o, p : -math.sin(math.pow(o, 2) + math.pow(p, 2)) + 1 # задаём функцию

x = np.linspace(0, 10, 10) # вычисляем диапазон значений по x
y = np.linspace(0, 10, 10) # вычисляем диапазон значений по y
X, Y = np.meshgrid(x, y) #Создаём сетки значений для x и для y

Z = [] # вычисляем значения функции z в точке (x,y)
for i in x:
    row = []
    for j in y:
        row.append(z(i,j))
    Z.append(row)
Z = np.reshape(
    Z, (-1, 10))
con = pl.contour(X, Y, Z) # строим контурный график
pl.show()

ax = pl.axes(projection='3d')
ax.plot_surface(X, Y, Z)
pl.show()

