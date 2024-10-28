import math
import scipy as sp
from matplotlib import pyplot as pl

f = lambda x: 3 * (x ** 2) - 100 * math.exp(-0.1 * x) # исходная функция

step = 0.01 # шаг деления для отображения графика
interval = (-37.2, 5) # приближённый интервал, где могут хрнаиться корни
x = [interval[0] + i * step for i in range(int(abs(interval[1] - interval[0])/ step))] # вычисление дискретных значений аргумента
y = [f(x_i) for x_i in x] # вычисление значений функции
ax = pl.gca() # настройка отображения осей по центру
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
pl.plot(x, y) # построение графика
approximate_x = [-37.3, -8.9, 4.6] # найдённые приближённые корни уравнения
pl.scatter(approximate_x, [f(x) for x in approximate_x]) # построение приближённых точек
solved_x = [sp.optimize.fsolve(f, x)[0] for x in approximate_x] # нахождение корней через fsolve
pl.scatter(solved_x, [f(x) for x in solved_x], c="red") # построение найденных корней
for x in solved_x:
    print(f'f({x})=',f(x)) # вывод значений корней в консоль
pl.show()