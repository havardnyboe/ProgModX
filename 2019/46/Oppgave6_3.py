import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

def f(x):
    y = -x**2+5*x-6
    return y

for i in np.arange(0,5,0.025):
    x.append(i)
    y.append(f(i))

xtop = x[y.index(max(y))]
ytop = max(y)

plt.grid()
plt.plot(x, y, label="$f(x)=x^2+5x-6$")
for i in x:
    if f(i) == 0:
        plt.plot(i, f(i), "ro", label="({}, {})".format(i, f(i)))
        print("Nullpunkt:", i)
plt.plot(xtop, ytop, "bo", label="({}, {})".format(xtop, ytop))
print("Toppunkt:", xtop, ytop)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()