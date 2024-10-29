import math

import numpy as np
from matplotlib import pyplot as pl
from scipy.fft import fft

dt = 0.0001
t = np.arange(0, 1, dt)
y = (2 * np.sin(2 * np.pi * t) + 3 * np.cos(2 * np.pi * 3 * t) +
     0.5 * np.sin(2 * np.pi * 10 * t) + np.random.randn(len(t)))

N = len(t)
Y = fft(y)

A = abs(2*Y/N)
fs = 1/dt
m = np.array(range(N))
f = m * fs / N

pl.subplot(1, 3, 1)
pl.plot(t, y, 'k')
pl.xlabel('t')
pl.ylabel('y(t)')

pl.subplot(1, 3, 2)
pl.plot(f, A, 'k')
pl.xlabel('f')
pl.ylabel('A(f)')

pl.subplot(1, 3, 3)
pl.stem(f, A, 'k')
pl.xlabel('f')
pl.ylabel('A(f)')
pl.show()