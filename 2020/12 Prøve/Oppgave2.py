from matplotlib import pyplot as plt
import numpy as np

# Pasienten får en konstant dose på 8 mL og skiller ut 5% (0.05) av medisinen per time.
# y' = 8 - 0.05y

k = 3
dt = 1/10**k 
t0 = 0
y0 = 0
t_max = 48+dt # derinerer en maks tid
t = [t0]
y = [y0]


def next_y(yn, dx):
    return yn + (8 - 0.05*yn) * dx # diferensialikningen til oppgava


for i in np.arange(t0+dt, t_max, dt):
    i = round(i, k) # runder av tiden så den blir lettere og iterere gjennom lista
    t.append(i)
    y.append(next_y(y[-1], dt)) # finner den neste y-verdien til funksjonen

print(t)

# b)
for i in t: # itererer gjennom t-lista
    if i == 24: # finner når tiden er 24 timer
        m = y[t.index(i)] # finner y-verdien med samme index som tiden

print('Etter den første dagen vil passienten ha {:.3f} mg medisin i kroppen'.format(m))

plt.plot(t, y) # plotter funksjonen
plt.grid()
plt.show()
