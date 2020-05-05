import random

kast_verdi = []
ant_seksere = 0

ant_kast = int(input("\nSkriv inn hvor mange ganger terningen skal kastes: "))
for kast in range(ant_kast):
	terning = random.randint(1, 6)
	if terning%6 == 0:
		ant_seksere+=1
	kast_verdi.append(terning)	

frekvens = ant_seksere/len(kast_verdi)

print("\nDu kastet {} seksere, som representerer {}% av kasta\n".format(ant_seksere, round(frekvens*100, 2)))

se_liste = input("Vil du se lista med terningkasta? (J/N): ")
if se_liste.upper() == "J":
	print(kast_verdi)