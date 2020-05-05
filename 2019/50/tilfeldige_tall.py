from pylab import *

N = 500 
x = linspace(0, 100, N)
shuffle(x)
y = [uniform(-1, 1) for i in x]

plot(x, y, '+')
show()