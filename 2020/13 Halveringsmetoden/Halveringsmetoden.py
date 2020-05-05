import numpy as np


def f(x):
    return np.log(x**4+4)-(1/2)*x

a = -10000
b =  10000
t = 1E-10
k = 0

while abs(b-a) > t:
    k += 1
    m = (a+b)/2
    if f(a) * f(m) < 0:
        b = m
    elif f(b) * f(m) < 0:
        a = m
    else: 
        break
print(m, k)

