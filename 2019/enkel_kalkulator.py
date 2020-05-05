i = 0

while i < 1:
	tall1 = float(input("Skriv inn et tall: "))
	tall2 = float(input("Skriv inn et tall: "))
	opperator = input("Velg opperator (+, -, *, /): ")

	if (opperator == "+"):
		print(tall1, "+", tall2, "=", tall1 + tall2)
	elif (opperator == "-"):
		print(tall1, "-", tall2, "=", tall1 - tall2)
	elif (opperator == "*"):
		print(tall1, "*", tall2, "=", tall1 * tall2)
	elif (opperator == "/"):
		print(tall1, "/", tall2, "=", tall1 / tall2)
	else:
		print("Ugyldig opperator!")
	fortsett = input("\n\nVil du kjøre programmet en gang til?(J/N): " )
	if (fortsett.upper() == "J"):
		i = 0
		if (i == 0):
			print("\n")
	elif (fortsett.upper() == "N"):
		i = 1
	else:
		print("Du skrev inn noe ugyldig, prøv igjen")