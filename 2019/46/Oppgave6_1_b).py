import matplotlib.pyplot as plt, numpy as np

x = []
y = []

def f(x):
    y = x**2 - 2*x
    return y

for i in np.arange(-10,12,0.5):
    x.append(i)
    y.append(f(i))

plt.grid()
plt.plot(x,y,"g", label="$f(x)=x^2-2x$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()