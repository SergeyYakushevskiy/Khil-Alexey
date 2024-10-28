import numpy as np
def get_values(step, f, interval): # функция получения значений передаваемой функции с шагом step
    x = [i * step for i in range(interval[0], int(interval[1] / step))] # вычисляются значения аргумента
    y = [f(x_i) for x_i in x] # создаётся список значений функции
    return (x, y) # передаётся кортеж из списка значений аргумента и функции от этого аргумента

f = lambda x : x ** 2 # Заданная функция
step = 0.01 # шаг
interval = (2, 8) # интервал нахождения
x, y = get_values(step, f, interval) # вычисление значений функции

trap = np.trapezoid(y, x)# вычисление определённого интеграла
print(trap)