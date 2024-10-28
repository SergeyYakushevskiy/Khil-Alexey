from matplotlib import pyplot as pl
import scipy as sp

num = [2, 1]
den = [2, 0.1, 1]
function = sp.signal.TransferFunction(num, den)
poles = function.poles
print('Полюса функции: ', *poles)
X = [num.real for num in poles]
Y = [num.imag for num in poles]

pl.scatter(X, Y)
pl.title('Полюса системы')
pl.xlabel('real(x)')
pl.ylabel('imag(x)')
pl.show()


step = sp.signal.step(function)
pl.title('Переходная характеристика')
pl.plot(step[0], step[1])
pl.xlabel('t, с')
pl.ylabel('Амплитуда')
pl.show()

bode = sp.signal.bode(function)
pl.plot(bode[0], bode[1])
pl.title('Амплитудно-частотная характеристика')
pl.show()

