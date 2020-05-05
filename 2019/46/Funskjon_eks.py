import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

def f(x):
    y = x**2-4*x+3
    return y

for i in np.arange(-2.5,6.5,0.25):
    x.append(i)
    y.append(f(i))

x_bunn = x[y.index(min(y))]
y_bunn = min(y)
print("Bunnpunkt: {}, {}".format(x_bunn, y_bunn))

plt.grid()
plt.plot(x, y, label="$f(x)=x^2-4x+3$")
plt.plot(x_bunn, y_bunn, "ro", label="{}, {}".format(x_bunn, y_bunn))
plt.legend()
plt.show()