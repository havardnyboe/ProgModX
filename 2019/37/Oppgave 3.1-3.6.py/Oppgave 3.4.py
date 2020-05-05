# a) Lag et program hvor du kan taste inn hvor mange poeng du har fått, 
# slik at programmet kan finne ut hvilken karakter du har fått og skrive ut denne.

# b) Utvid programmet til å kunne brukes på alle matteprøver. 
# Brukeren må da i tillegg oppgi hvor mange poeng som var mulig å få på den aktuelle prøven.

max_poeng = int(input("Skriv inn maks antall poeng: "))
poeng = int(input("Skriv inn antall poeng:      "))

if (poeng > max_poeng):
	print("Du skrev inn noe ugyldig, prøv igjen!")
elif (poeng >= max_poeng * (56/60)):
	print("Karaker: 6")
elif (poeng >= max_poeng * (45/60)):
	print("Karakter: 5")
elif (poeng >= max_poeng * (35/60)):
	print("Karakter: 4")
elif (poeng >= max_poeng * (24/60)):
	print("Karakter: 3")
elif (poeng >= max_poeng * (12/60)):
	print("Karakter: 2")
elif (poeng <= max_poeng * 12/60) and (poeng >= 0):
	print("Karakter: 1")
elif (poeng < 0):
	print("Poeng kan ikke være negativt, prøv igjen!")
else:
	print("Du skrev inn noe ugyldig, prøv igjen!")