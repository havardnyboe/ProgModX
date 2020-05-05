alder = int(input("Skriv inn alder: "))
hoyde = int(input("Skriv inn høyde: "))

if alder >= 16 or (alder >= 14 and hoyde >= 160):
	print("Du kan ta karusellen!")
elif alder >= 14 and hoyde <160:
	print("Du kan ta karusellen med en voksen!")
else:
	print("Du kan ikke ta karusellen!")