from matplotlib import pyplot as plt
import numpy as np

k = 3
dt = 1/10**k
t0 = 0.0
s0 = 0.0
v0 = 26.0
t = [t0]
s = [s0]
v = [v0]

def strekning(sn, dx):
    return sn + (26-0.08*sn) * dx

def fart(sn):
    return 26 - 0.08*sn

for i in np.arange(t0+dt, 5+dt, dt):
    i = round(i, k)
    t.append(i)
    s.append(strekning(s[-1], dt))

for sn in s:
    if sn != s0:
        v.append(fart(sn))

for i in t:
    if i == 1:
        print('Etter en time har han syklet {:.2f} km'.format(s[t.index(i)]))

plt.plot(t, v, label="$v(t)=26-0.08*s(t)$")
plt.plot(t, s, label="$s(t)=sn + (26-0.08*sn) * dx$")
plt.legend()
plt.grid()
plt.show()
