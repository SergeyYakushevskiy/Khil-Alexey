from matplotlib import pyplot as pl

f = lambda x: x + 1 # задаются 2 произвольные функции
g = lambda x: x ** 2

x = [i for i in range (1, 10)] # интервал значений аргументов от 1 до 9 с шагом 1

pl.plot(x, [g(o) for o in x], label='Гипербола', c='red') # построение графика функции f
pl.plot(x, [f(x_i) for x_i in x], label='Экспоненциальная функция') # построение графика функции g
ax = pl.gca() # настройка отображения осей по центру
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
pl.legend() # включение отображения легенд
pl.show() # отображение окна графиков


pl.subplot(1, 2, 1) # задаётся окно, разделённое на 2 системы координат. На первом строится график g
pl.plot(x, [g(o) for o in x], label='Гипербола', c='red')
pl.xlabel('x')
pl.ylabel('y')
pl.legend()

pl.subplot(1, 2, 2) # на втором строится график функции f
pl.plot(x, [f(x_i) for x_i in x], label='Экспоненциальная функция')
pl.xlabel('x')
pl.ylabel('y')
pl.legend()

pl.show()
