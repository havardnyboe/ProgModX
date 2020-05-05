import numpy as np
import matplotlib.pyplot as plt

volum = (int(input("Skriv inn volum i liter: ")))/1000
def_hoyde = input("Definer en høyde (hvis nei skriv n): ")
radius = []
areal = []

def h(volum, r):
    return volum/(np.pi*r**2)

def A(r):
    return np.pi*r*(r+2*h(volum, r))

for i in np.arange(0.1, 5, 0.01):
    radius.append(i)
    areal.append(A(i))

# Utregning av mål og pris #
min_areal = round(min(areal), 2)
min_radius = round(radius[areal.index(min(areal))], 2)
min_hoyde = round(h(volum, radius[areal.index(min(areal))]), 2)
if def_hoyde.upper() != "N":
    for r in radius:
        if round(h(volum, r), 1) == float(def_hoyde):
            min_radius = round(r, 2)
            min_areal = round(areal[radius.index(r)], 2)
            min_hoyde = round(h(volum, r), 1)

tot_pris_materialer = (173*min_areal) + 3000
if tot_pris_materialer > 4500:
    tot_pris_materialer -= tot_pris_materialer * 0.1

# Utskrift til konsoll #
print("""\n~~~~~~ Optimale mål ~~~~~~
areal:  {}m^2
radius: {}m
høyde:  {}m
~~~~~~~~~~~~~~~~~~~~~~~~~~\n
~~~~~~ Kostnader ~~~~~~~~~
Pris per kv.m:  173 kr
Pris på arbeid: 3000 kr
Totalpris     : {} kr
~~~~~~~~~~~~~~~~~~~~~~~~~~\n""".format(min_areal, min_radius, min_hoyde, round(tot_pris_materialer, 2)))

# Plotting #
plt.plot(radius, areal, color="#3d5e7f")
plt.plot(min_radius, min_areal, "bo")

plt.title("Badestampfabrikken")
plt.xlabel("Radius")
plt.ylabel("Areal")

plt.show()