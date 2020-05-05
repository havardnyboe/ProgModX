innskudd = int(input("Skriv inn en startinvistering: "))
rente = int(input("Skriv inn renter: "))
uttak = int(input("Hvor mye ønsker du å ende opp med?: "))
rente = rente/100
sluttverdi = innskudd
teller_slutt = 100

while sluttverdi < uttak:
	p_rente = sluttverdi/rente
	sluttverdi += p_rente

print("\n\n{}".format(sluttverdi))