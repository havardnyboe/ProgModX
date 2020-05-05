# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:00:48 2020

@author: ola0907
"""
# Importerer biblioteker
import matplotlib.pyplot as plt
import csv
import math

# Oppretter lister som skal fylles med tabellverdier
tid = []        # tid, x-aksen
x_aks = []      # akselerasjon i x-retning
y_aks = []      # akselerasjon i y-retning
sum_aks = []    # lengden av akselerasjonsvektoren
fart_x = [10]   # fart i x-retning, med initialverdi lagt inn som element nr 0.
fart_y = [10]   # fart i y-retning, med initialverdi lagt inn som element nr 0.
pos_x = [0]     # posisjon i x-retning, med initialverdi lagt inn som element nr 0.
pos_y = [0]     # posisjon i y-retning, med initialverdi lagt inn som element nr 0.
fart = [14.14]  # lengden av fartsvektoren, med initialverdi lagt inn som element nr 0
posisjon =[0]   # lengden av posisjonsvektoren, med initialverdi lagt inn som element nr 0



# Åpner og leser filen med akselerasjonsdata, samt legger verdiene i lister
with open('2020/17 -20 Innleveringsoppgave/akselerasjonsdata_semi.csv') as csv_file: # åpner csv-filen med dataene
    aks_fil = csv.reader(csv_file, delimiter = ";")  # leser fila og tilordner innholdet i fila til en variabel, angir semikolon som skilletegn mellom elementene
    linjeteller = 0                             # initierer variabel for telling av antall linjer
    for linje in aks_fil:                       # Itererer gjennom filen linje for linje
        if linjeteller == 0:                    # Overskriftene står i linje nummer 0
            pass                                # Hopp ut av iterasjonen hvis linjenummer = 0
        else:
            tid.append(float(linje[0]))         # legger til element 0 (tid) i linje nr 'linje'.  
            x_aks.append(float(linje[1]))       # legger til element 1 (x-retning) i linje nr 'linje'.
            y_aks.append(float(linje[2]))       # legger til element 2 (y-retning) i linje nr 'linje'.
        linjeteller += 1                        # øker linjetelleren med 1 når vi er ferdige med å hente ut overskriftene


dt = tid[1]-tid[0] # Definerer delta t som tidsdifferansen mellom de to første målingene 

# Funksjon som regner ut og returnerer lengden av en vektor
def lengde(x,y,i):
    return math.sqrt(x[i]**2 + y[i]**2)

# Løkke som fyller listen med samlet akselearsjon (lengden av akselerasjonsvektoren)
for i in range(len(tid)):
    sum_aks.append(lengde(x_aks,y_aks,i))

# Eulers metode. Funksjoner som skal brukes til å fylle listene med verdier 
def neste_fart(v,a,n,dt):       # Funksjon som beregner neste fartsverdi vha Eulers metode
    return v[-1]+a[n]*dt        # forrige element i fartslista + nåværende akselerasjon ganger delta-t.

def neste_posisjon(s,v,n,dt):   # Funksjon som beregner neste posisjonsverdi vha Eulers metode
    return s[-1]+v[n]*dt        # forrige element i posisjonslista + nåværende fart ganger delta-t.


# Løkke som fyller listene med verdier
for i in range(len(tid)-1):                                 # antall ganger løkka kjøres er en mindre enn ant. elementer, siden det ligger en verdi i lista fra før
    fart_x.append(neste_fart(fart_x,x_aks,i,dt))            # legger til verdi lista fart_x vha Eulers metode
    fart_y.append(neste_fart(fart_y,y_aks,i,dt))            # legger til verdi lista fart_y vha Eulers metode
    pos_x.append(neste_posisjon(pos_x,fart_x,i,dt))         # legger til verdi lista pos_x vha Eulers metode
    pos_y.append(neste_posisjon(pos_y,fart_y,i,dt))         # legger til verdi lista pos_y vha Eulers metode
    fart.append(lengde(fart_x,fart_y,i))     # legger til verdi lista fart ved å regne ut lengden av vektorsummen
    posisjon.append(lengde(pos_x,pos_y,i))   # legger til verdi lista posisjon ved å regne ut lengden av vektorsummen
    
# Plotting
plt.plot(tid,fart,label="Fart")
plt.plot(tid,posisjon,label="Posisjon")
plt.plot(tid,sum_aks, label = "Samlet akselerasjon")
#plt.plot(tid,fart_x,label="fart i x-retning")
#plt.plot(tid,fart_y,label="fart i y-retning")
#plt.plot(tid,pos_x,label="posisjon i x-retning")
#plt.plot(tid,pos_y,label="posisjon i y-retning")
plt.xlabel("Tid, sekunder")
plt.ylabel("Akselerasjon, fart, posisjon.")
plt.title("Farten og posisjonen til partikkelen")
plt.grid()
plt.legend()
plt.show()


