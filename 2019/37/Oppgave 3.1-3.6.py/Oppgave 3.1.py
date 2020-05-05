# a) Lag et program som spør brukeren om alderen til brukeren.
# Skriv ut en kommentar som avhenger av om alderen er under eller over 18 år.
# b) Utvid programmet til å skille mellom flere aldre.

alder = int(input("Skriv inn din alder: "))

if (alder >= 18):
	print("Du kan ta lappen!")
elif (alder >= 16):
	print("Du kan øvelseskjøre!")
else:
	print("Du kan ikke øvelseskjøre!")

