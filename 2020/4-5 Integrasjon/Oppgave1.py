from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
A_v = 0
A_h = 0
A_m = 0
x = []
y = []


def f(x):
    return x**2


for i in np.arange(0, 2+dx, dx):
    x.append(i)
    y.append(f(i))
    A_v += f(i)*dx
    A_h += f(i+dx)*dx
    A_m += f(i+dx/2)*dx

print("Arealet under grafen er {:.4f} med vestresum".format(A_v))
print("Arealet under grafen er {:.4f} med høyresum".format(A_h))
print("Arealet under grafen er {:.4f} med midtsum".format(A_m))

# quit()

plt.grid()
plt.bar(x, y, dx)
plt.plot(x, y, "r")
plt.show()
