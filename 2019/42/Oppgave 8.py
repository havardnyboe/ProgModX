liste = ["Tekst", 42, 3.1415, True, [1, 2], (2, 3)]
neste = 0

for i in liste:
    print(i, "er en", type(liste[neste]))
    neste+=1