import matplotlib.pyplot as plt, math

x = []
y = []
z = []

for i in range(5):
    x.append(i)

for elem in x:
    y.append(elem**2)

for elem in x:
    z.append(elem**3)

plt.plot(x, y, label="$f(x)=x^2$")
plt.plot(x, z, label="$f(x)=x^3$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Andregradsfunksjon")
plt.legend()
plt.grid()
plt.show()