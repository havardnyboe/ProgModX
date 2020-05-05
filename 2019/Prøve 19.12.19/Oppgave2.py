# Prøve i ProgMod 19.12.19, Håvard 2STG
# Del 2

# Oppgave 2

# a)
# bruker Pythagoras' læresetning: h = sqrt(k_1**2 + k_2**2)
# h_1 = sqrt(x**2+90**2)
# h_2 = sqrt(200-x)**2 + 60**2
# d(x) = sqrt(x**2+90**2)+sqrt((200-x)**2+60**2)

# b) 
from matplotlib import pyplot as plt # importerer pyplot fra matplotlib-bibloteket
import numpy as np # importerer numpy-bibloteket

x = []
y = []

def d(x): # definerer funksjonen
    return np.sqrt((x**2) + (90**2)) + np.sqrt(((200-x)**2) + (60**2))

for i in np.arange(0, 300, 0.1): # teller fra 0 til 300 fordi gangavstanden ikke kan være negativ
    x.append(i) # legger x-verdier i lista
    y.append(d(i)) # legger y-verdier i lista
plt.plot(x, y, "g--", label="$sqrt(x^2+90^2)+sqrt((200-x)^2+60^2)$") # plotter grafen

# c)
y_min = min(y) # finner den minste y-verdien
x_min = x[y.index(min(y))] # finner x-verdien med samme index som den minste y-verdien
plt.plot(x_min, y_min, "ro", label=(x_min, y_min)) # plotter punktet

print("\nB ligger {} meter unna parkeringsplassen\n".format(np.sqrt(90**2+x_min**2)))

# d)
for i in range(len(y)): # kjører like mange ganger som det er elementer i lista
    if round(y[i], 2) == 280: # hvis et element i y-lista er lik 280
        plt.plot(x[i], y[i], "bx", label=(round(x[i], 2), round(y[i], 2))) # plotter punktet
        print("\nAB må være {} meter unna parkeringen for at avstanden de må gå blir 280 meter\n".format(round(x[i], 2)))

plt.grid() # lager rutenett
plt.xlabel("Lengden AB")
plt.ylabel("Total avstand")
plt.title("Hyttetur til fjellet")
plt.legend() # viser 'labelene' til grafen og punktene

plt.show() # viser koordinatsystemet