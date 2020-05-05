from matplotlib import pyplot as plt
import numpy as np

dt = 1E-2
t = []
y = []
t_max = 10+dt

def deriver(f, x, dx):
    return (f(x+dx)-f(x))/dx # funksjon for å derivere

def s(t):
    return 2*t**2 + 4*t # funksjonen til oppgaven

for i in np.arange(0, t_max, dt):
    t.append(i)
    y.append(deriver(s, i, dt)) # deriverer strekningen

# b)
# 100km/h = 100/3.6 = 27.78 m/s

v = 0
for i in y:
    if i <= 27.78: #finner når farten er omtrent 27.78 m/s
        v = i

tid = t[y.index(v)] # finner tiden med samme index som farten

print('Bilen bruker {:.2f} sekunder på å komme opp i en fart på 100km/h'.format(tid))

plt.plot(t,y) # plotter grafen
plt.grid()
plt.show()