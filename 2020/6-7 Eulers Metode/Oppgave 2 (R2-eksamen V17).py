from matplotlib import pyplot as plt
import numpy as np

# a) pasienten får en konstant dose på 3.0mg og skiller ut 30% (0.30) av medisinen per time.
# y' = -0.30y + 3.0

# b)
dt = 1E-4
t0 = 0
y0 = 0
t_max = 24*7 + dt
t = [t0]
y = [y0]


def next_y(yn, dx):
    return yn + (-0.30*yn+3.0) * dx


for i in np.arange(t0+dt, t_max, dt):
    t.append(i)
    y.append(next_y(y[-1], dt))

# c)
print('Etter lang tid ({:.1f} dager) vil passienten ha {:.3f} mg medisin i kroppen'.format(
    (t_max-dt)/24, y[-1]))

# d)


plt.plot(t, y)
plt.grid()
plt.show()
