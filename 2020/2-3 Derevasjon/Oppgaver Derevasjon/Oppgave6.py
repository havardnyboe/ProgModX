from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
x_verdier = []
u_verdier = []
u_derivert = []
v_verdier = []
v_derivert = []
hs = []
vs = []


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


def deriver_u_v():


def u(x):
    return np.sin(1/x**2)


def v(x):
    return np.sqrt(np.log(x))


for i in np.arange(1 + dx, 5 + dx, dx):
    x_verdier.append(i)
    u_verdier.append(u(i))
    u_derivert.append(deriver(u, i, dx))
    v_verdier.append(v(i))
    v_derivert.append(deriver(v, i, dx))

for i in range(len(x_verdier)):
    hs.append((u_derivert[i]*v_verdier[i])+(u_verdier[i]*v_derivert[i]))

# plt.plot(x_verdier, hs)
plt.plot(x_verdier, vs)
plt.grid()
plt.show()
