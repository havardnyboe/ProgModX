i=0

while i < 1:
	for j in range(int(input("Skriv inn antall ganger løkken skal kjøre: "))):
		print("Du er god!")

	svar = input("Skal programmet kjøre igjen? (J/N): ")
	if svar.upper() == "J":
		i=0
	else:
		i=1	