from matplotlib import pyplot as plt 
import numpy as np

x = []
y = []
n_punkter = []

def f(x):
    return x**2 - 5*x + 6

for i in np.arange(-4, 10, 0.5):
    x.append(i)
    y.append(f(i))
plt.plot(x,y, label='$f(x)=x^2-5x+6$')

for i in range(len(y)):
    if round(y[i], 2) == 0:
        n_punkter.append(x[i])
        plt.plot(x[i], y[i], 'ro')
print(n_punkter)

plt.grid()
plt.title('Andregradsfunsjon')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()