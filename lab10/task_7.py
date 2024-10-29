import numpy as np
from matplotlib import pyplot as pl
from scipy.fft import fft

dt = 0.0001 # задаём шаг деления отрезка
t = np.arange(0, 1, dt) # вычисляем значения на отрезке от 0 до 1 с шагом t
y = (2 * np.sin(2 * np.pi * t) + 3 * np.cos(2 * np.pi * 3 * t) +
     0.5 * np.sin(2 * np.pi * 10 * t) + np.random.randn(len(t))) # задаём гармоническую функцию

N = len(t) # вычисляем количество точек
Y = fft(y) # быстрое преобразование фурье

A = abs(2*Y/N) # амплитуда составляющей спектра
fs = 1/dt # дисккрета по частоте
m = np.array(range(N))
f = m * fs / N # составляющая спектра

pl.subplot(1, 3, 1) # построение спектра
pl.plot(t, y, 'k')
pl.xlabel('t')
pl.ylabel('y(t)')

pl.subplot(1, 3, 2) # график дискретного амплитудно-частотного спектра
pl.plot(f, A, 'k')
pl.xlabel('f')
pl.ylabel('A(f)')

pl.subplot(1, 3, 3)
pl.stem(f, A, 'k')
pl.xlabel('f')
pl.ylabel('A(f)')
pl.show()