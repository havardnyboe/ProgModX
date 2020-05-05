import numpy as np

dx = 1E-4
sigma = 1


def f(x):
    return (1/(np.sqrt(2*np.pi)))*np.e**(-(x**2/2))


for k in np.arange(1.2, 3.1, 1.8):
    integral = 0
    for x in np.arange(-k*sigma, k*sigma+dx, dx):
        integral += f(x+dx/2) * dx
    print(integral)
