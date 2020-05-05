import numpy as np

a = 0
b = 5


def f(x):
    return x**2


def A_v():
    A = 0
    for x in np.arange(a, b, dx):
        A += f(x) * dx
    return A


def A_h():
    A = 0
    for x in np.arange(a, b, dx):
        A += f(x + dx) * dx
    return A


def A_m():
    A = 0
    for x in np.arange(a, b, dx):
        A += f(x + dx/2) * dx
    return A


for i in range(5, 7):
    dx = 1E0
    print("\n\nOppgave {}".format(i))
    for i in range(3):
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~
dx = {}, a = {}, b = {}

Venstresummering:   {:.3f}
Høyresummering:     {:.3f}
Midtsummering:      {:.3f}""".format(dx, a, b, A_v(), A_h(), A_m()))
        dx = dx/10
    a = -5
    b = 0
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
