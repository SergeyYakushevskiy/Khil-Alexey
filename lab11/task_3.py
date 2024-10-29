import numpy as np
import scipy as sp


def system(t, q): # диф. уравнение второго порядке сводится к системе уравнений
    x, y = q

    dx = y
    dy = -x * y - x

    return [dx, dy]


t_end = 20
t = np.linspace(0, t_end, 100) # область определения
x0, y0 = 10, 5 # начальные приближения

ode = sp.integrate.solve_ivp(system, [0, t_end], [x0, y0], method='RK23', dense_output=True) # решение диф.
                                                                                                        # уравнения методом Рунге-Кутты 3го порядка


res = ode.sol(t) # вычисление численного решения

x, y = res[0], res[1]
# вывод результатов
print(x)
print(y)


