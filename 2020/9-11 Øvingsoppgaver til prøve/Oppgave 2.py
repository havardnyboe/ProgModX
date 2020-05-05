from matplotlib import pyplot as plt
import numpy as np

dt = 1E-1
t_verdier = []
s_verdier = []
v_verdier = []
a_verdier = []


def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx


def s(t):
    return t**3 + (1/3)*t


def v(t):
    return deriver(s, t, dt)


def a(t):
    return deriver(v, t, dt)


for i in np.arange(0, 120, dt):
    t_verdier.append(i)
    s_verdier.append(s(i))
    v_verdier.append(v(i))
    a_verdier.append(a(i))


fig, axs = plt.subplots(1, 3, constrained_layout=True, sharex=True)
axs[0].plot(t_verdier, s_verdier)
axs[0].grid()
axs[0].set_title('s(t)')

axs[1].plot(t_verdier, v_verdier)
axs[1].grid()
axs[1].set_title('v(t)')

axs[2].plot(t_verdier, a_verdier)
axs[2].grid()
axs[2].set_title('a(t)')

plt.show()
