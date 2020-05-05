from matplotlib import pyplot as plt
import numpy as np

def f(x):
    y = np.sqrt(x)
    return y

x_val = []
y_val = []

for x in np.arange(0,5,0.01):
    x_val.append(x)
    y_val.append(f(x))

plt.xkcd()
plt.plot(x_val, y_val, label="$f(x)=\sqrt{x}$")

plt.title("Kvadratroten av x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.tight_layout()

plt.show()
