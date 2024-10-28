import math

import matplotlib.pyplot as pl


def plot(x, y, xlabel='x', ylabel='f(x)', title=''): # функция построения графика. Передаётся список точек по Ох
                                                     # список значений функции в этих точках, подписи для осей и название
                                                     # графика
    pl.plot(x, y) # построим график
    pl.xlabel(xlabel) # зададим подпись для Ох
    pl.ylabel(ylabel) # подпись для Оу
    pl.title(title) # название
    pl.show() # отобразим в виде окна

def get_values(step, f): # функция получения значений передаваемой функции с шагом step
    x = [interval[0] + i * step for i in range(int(interval[1] / step))] # вычисляются значения аргумента
    y = [f(x_i) for x_i in x] # создаётся список значений функции
    return (x, y) # передаётся кортеж из списка значений аргумента и функции от этого аргумента

step = 0.01 # задаётся шаг деления Ох
interval = (0, 2*math.pi) # интервал нахождения значений функции

f = lambda  x : math.sin(x) # синус
x, y = get_values(step, f) # получение значений
plot(x, y, title='f(x)=sin(x)') # построение графика

f = lambda x : math.tan(x) # тангенс
x, y = get_values(step, f)
plot(x, y, title='f(x)=tg(x)')

f = lambda x : x + 1 if x < 5 else x ** 2 # составная функция
x, y = get_values(step, f)
plot(x, y, title='f(x)= x + 1 if x < 5 else x^2')

