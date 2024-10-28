from random import randint
from matplotlib import pyplot as pl

array_1 = [randint(1, 10) for i in range(5)] # массив из 5 случайных значений
array_2 = [randint(1, 10) for i in range(5)] # второй массив
array_leg = [f'A{i}' for i in range(1, 6)] # сгенерированный массив подписей
pl.bar(array_leg, array_1, label='1ый массив') # построение диаграмм
pl.bar(array_leg, array_2, label='2ой массив')
pl.legend() # добавление легенд
pl.show()

