from matplotlib import pyplot as plt
import numpy as np

dx = 1E-2
# variabler for f
x_f = []
y_f = []
A_f = 0
# variabler for g
x_g = []
y_g = []
A_g = 0

def f(x):
    return np.cos(x) # funksjonen f

def g(x):
    return 1 - ((3/4)*x)**2 # funksjonen g


# for-løkke for f
for i in np.arange(-(np.pi/2), (np.pi/2), dx): # definisjonsmengden til f
    x_f.append(i)
    y_f.append(f(i))
    A_f += f(i+dx/2)*dx # integral til f

#for-løkke for g
for i in np.arange(-(4/3), (4/3), dx): # definisjonsmengden til g
    x_g.append(i)
    y_g.append(g(i)) 
    A_g += g(i+dx/2)*dx # integral til g

print('Arealet til f er {:.4f}'.format(A_f))
print('Arealet til g er {:.4f}'.format(A_g))

# finner ut hvilket areal som er størst og skriver det ut
if A_f > A_g:
    a = A_f
else:
    a = A_g

print('Arealet {:.4f} er størst'.format(a))

# plotter grafene i to subplots
fig, axs = plt.subplots(1, 2, constrained_layout=True, sharex=True, sharey=True)
# subplot til f
axs[0].bar(x_f, y_f, dx)
axs[0].plot(x_f, y_f, "r")
axs[0].grid()
axs[0].set_title('f(x)')
# subplot til g
axs[1].bar(x_g, y_g, dx)
axs[1].plot(x_g, y_g, "r")
axs[1].grid()
axs[1].set_title('g(x)')

plt.show()
