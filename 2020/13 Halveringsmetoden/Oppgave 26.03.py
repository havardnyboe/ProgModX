import numpy as np

# 4*e^(3x-2)=244
# 4*e^(3x-2)-244=0

def f(x):
    return 4*np.e**(3*x-2)-244

a = -100
b =  100
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

print("\nNullpunktet ligger på ({:.3f}, {:.0f}) \nLøkken kjørte {} ganger\n".format(m, f(m), k))
