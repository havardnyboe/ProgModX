import matplotlib.pyplot as plt

dager = []
helgeroa = [-1, 1, 2, 3, 6, 5, 6, 5]
geneve = [7, 7, 7, 8, 8, 7, 8, 5]
honlulu = [26, 26, 28, 27, 28, 27, 27, 26]

for i in range(1, 9): dager.append(i)

plt.grid()
plt.xlabel("Dager")
plt.ylabel("$Grader^oC$")
plt.plot(dager, helgeroa, "r.-", label="Helgeroa")
plt.plot(dager, geneve, ".-", label="Genève")
plt.plot(dager, honlulu, ".-", label="Honlulu")
plt.legend()
plt.show()