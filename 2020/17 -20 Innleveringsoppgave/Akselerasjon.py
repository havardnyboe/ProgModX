# impoerterer bibloteker
import csv
import matplotlib.pyplot as plt
import numpy as np

dt = 0.1  # delta t
# lager tomme lister som skal fylles med data fra csv dokumentet
t = []
a_x = []
a_y = []
a = []
# lager lister for bereging av fart
v_x = [10]
v_y = [10]
v = []
# lager lister for bereging av streking
s_x = [0]
s_y = [0]
s = []

def lengde_vektor(arr_1, arr_2, i):  # funksjon for å regne ut lengden av en vektor
    return np.sqrt(arr_1[i]**2 + arr_2[i]**2)

def euler(arr_1, arr_2, i, dx):  # funksjon som bruker eulers metode
    return arr_1[-1]+arr_2[i]*dx


with open("2020/17 -20 Innleveringsoppgave/akselerasjonsdata_semi.csv", "r") as csv_file:  # åpner csv filen
    askelerasjon_data = csv.reader(csv_file, delimiter=";")
    i = 0  # teller for linjenummer
    for l in askelerasjon_data:
        if i == 0:  # leser navnene fra første linjen i dokumentet
            x_navn = str(l[0])  # tilordner x_navn navnet til x-asken
            y1_navn = str(l[1])  # tilordner y1_navn navnet til a_x grafen
            y2_navn = str(l[2])  # tilordner y2_navn navnet til a_y grafen
        else:
            t.append(float(l[0]))  # legger til sekundene i t-lista
            a_x.append(float(l[1]))  # legger til x-retning i a_x lista
            a_y.append(float(l[2]))  # legger itl y-retning i a_y lista
        i += 1

for i in range(len(t)):
    # legger til fart i fartlista med Eulers metode
    v_x.append(euler(v_x, a_x, i, dt))
    # legger til fart i fartlista med Eulers metode
    v_y.append(euler(v_y, a_y, i, dt))
    # legger til strekning i strekninglista med Eulers metode
    s_x.append(euler(s_x, v_x, i, dt))
    # legger til strekning i strekninglista med Eulers metode
    s_y.append(euler(s_y, v_y, i, dt))
    # regner ut den totale akselerasjonen og legger den til i lista
    a.append(lengde_vektor(a_x, a_y, i))
    # regner ut den totale farten og legger den til i lista
    v.append(lengde_vektor(v_x, v_y, i))
    # regner ut den totale strekningen og legger den til i lista
    s.append(lengde_vektor(s_x, s_y, i))

# oppg a) og b)

# strekningsgrafen viser totalt tilbakelagt strekning over tid så siste element vil være den totale strekningen
tot_s = s[-1]

ant_m = 5  # definerer antall meter jeg skal finne
for i in range(len(s)):
    if s[i] <= ant_m:  # finner når partikkelen har beveget seg 5 meter
        # finner tiden etter at partikelen har bevegd seg 5 meter
        t_etter_ant_m = t[i]

print("\nPartikkelen har beveget seg totalt {:.2f} meter".format(tot_s))
print("\nPartikkelen brukte {:.2f} sekunder på å bevege seg omtrent {} meter".format(
    t_etter_ant_m, ant_m))
print("\nMaks fart var {:.2f} m/s og intraff etter {:.2f} sekunder".format(
    max(v), t[v.index(max(v))]))

## PLOTTING AV GRAFER ##

# lager subplotene og definerer størrelsen på de
fig, axs = plt.subplots(1, 2, constrained_layout=True, figsize=(12, 5))
# Grafikkfelt for askelerasjonen til partikelen
axs[0].plot(t, a_x, label=y1_navn)  # plotter akselerasjonen i x-retning
axs[0].plot(t, a_y, label=y2_navn)  # plotter akselerasjonen i y-retning
axs[0].plot(t, a, label="Akselerasjon")  # plotter akselerasjonen
axs[0].set_title("Akselerasjonen etter 10s", fontsize=14)

# Grafikkfelt for Strekning, Fart og Akselerasjon til partikelen
axs[1].plot(t, s, label="Strekning")  # plotter strekningen
axs[1].plot(t, v, label="Fart")  # plotter farten
axs[1].plot(t, a, label="Akselerasjon")  # plotter akselerasjonen
axs[1].set_title("Strekning, Fart og Akselerasjon etter 10s", fontsize=14)

# setter på navn på aksene og rutenett på begge grafikkfeltene
for i in range(2):
    axs[i].set_xlabel(x_navn + " (sekunder)")
    axs[i].set_ylabel("Akselerasjon (m/s)")
    axs[i].grid()
    axs[i].legend()

# viser figuren
plt.show()
