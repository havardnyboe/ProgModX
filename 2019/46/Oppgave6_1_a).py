import matplotlib.pyplot as plt, numpy as np

x = []
y = []

def f(x):
    y = 2*x + 1
    return y

for i in np.arange(0,5,0.5):
    x.append(i)
    y.append(f(i))

plt.grid()
plt.plot(x,y, "--", label="f(x)=2x+1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()