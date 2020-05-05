import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

def f(x):
    y = 4-0.125*x**3
    return y

for i in np.arange(0, 2*np.cbrt(4), 0.1):
    x.append(i)
    y.append(f(i))


plt.grid()
plt.plot(x, y, "--", label="$f(x)=4-0.125x^3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()