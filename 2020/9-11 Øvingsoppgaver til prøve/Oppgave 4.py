from matplotlib import pyplot as plt
import numpy as np

k = 2
dx = 1/(10**k)
x = []
y = []
A = 0
V = 0


def f(x):
    return np.sqrt(x**2-x**4)


for i in np.arange(-1, 1+dx, dx):
    i = round(i, k)
    x.append(i)
    y.append(f(i))
    if i != 1:
        A += f(i+dx/2)*dx
    V += np.pi*f(i)**2*dx

print('Areal = {:.4f}'.format(A))
print('Volum = {:.4f}'.format(V))

plt.bar(x, y, dx, label="$\int_{-1}^1\sqrt{x^2-x^4}$")
plt.plot(x, y, "r", label="f(x)=$\sqrt{x^2-x^4}$")
plt.grid()
plt.legend()
plt.show()
