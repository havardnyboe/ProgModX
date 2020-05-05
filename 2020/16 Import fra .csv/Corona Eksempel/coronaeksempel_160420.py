# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:02:17 2020

@author: ola0907
"""

import csv
import matplotlib.pyplot as plt

dag = []
antall =[]

with open("2020/16 Import fra .csv/Corona Eksempel/coronadata.csv") as csv_file:        # åpner csv-filen med dataene
    corona = csv.reader(csv_file, delimiter = ";")  # tilordner innholdet i fila til en variabel, angir komma som skilletegn mellom elementene
    linjeteller = 0                             # initierer variabel for telling av antall linjer
    for linje in corona:                        # Itererer gjennom filen linje for linje
        if linjeteller == 0:         # Overskriftene står i linje nummer 0
            x_navn = str(linje[0])   # definerer overskrift x-akse som element 0 i linje 0
            y_navn = str(linje[1])   # definerer overskrift y-akse som element 1 i linje 0
        else:
            dag.append(int(linje[0]))  # legger til element 0 (dag) i linje nr 'linje'.  
            antall.append(int(linje[1])) # legger til element 1 (antall) i linje nr 'linje'.
        linjeteller += 1              # øker linjetelleren med 1 når vi er ferdige med å hente ut overskriftene



plt.plot(dag,antall)
plt.title("Påvist Covid19-smittede i Norge etter 20. februar." )
plt.grid()
plt.xlabel(x_navn)
plt.ylabel(y_navn)
plt.show()
