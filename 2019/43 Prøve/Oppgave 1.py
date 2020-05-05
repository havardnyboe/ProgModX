import math

kule_radius = 2.5 # radius på 2,5cm
volum_kule = (4*math.pi*kule_radius**3)/3 # volumet for en kule
tot_volum_is = 3000 # is beholderen har et volum på 3 liter eller 3000cm^3
ant_kuler = 0 # variabel for antall kuler
ant_kuler_volum = 0.0 # variabel for å volumet til antall kuler

while ant_kuler_volum < tot_volum_is: # så lenge totalvolumet til kulene er mindre enn totalvolumet til isboksen
    ant_kuler_volum += volum_kule
    ant_kuler += 1

print("\n{} liter is vil gi {} kuler med is\n".format(tot_volum_is/1000, ant_kuler))