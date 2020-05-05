from matplotlib import pyplot as plt
import numpy as np

k = 3
dt = 1/10**k
t0 = 0.0
y0 = 100.0
t = [t0]
y = [y0]


def next_y(yn, dx):
    return yn + (-np.sqrt(yn)) * dx


i = 0
while y[-1] >= 0:
    i = round(i+dt, k)
    t.append(i)
    y.append(next_y(y[-1], dt))
y.pop()
t.pop()

print('Det tar {} sekunder før tanken er tom'.format(t[-1]))

plt.plot(t, y)
plt.grid()
plt.show()
