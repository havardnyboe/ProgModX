from matplotlib import pyplot as plt
import numpy as np

dt = 1E-4
t6 = 6
y6 = 9.17
t_min = 0-dt
t = [t6]
y = [y6]


def last_y(yn, dx):
    return yn - (-0.30*yn+3.0) * dx


for i in np.arange(t6-dt, t_min, -dt):
    t.append(i)
    y.append(last_y(y[-1], dt))

print('y0 = {:.3f}'.format(y[-1]))
plt.plot(t, y)
plt.grid()
plt.show()
