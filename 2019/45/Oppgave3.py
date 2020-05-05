import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y, ":", label="$f(x)=sin(x)$")
plt.plot(x, z, "-.", label="$g(x)=cos(x)$")
plt.legend()
plt.show()