i=0

while i < 1:	
	antall = int(input("Skriv inn antall ganger løkken skal kjøres: "))
	j = 0

	while j < antall:
		print("Du er god!")
		j+=1

	svar = input("Skal programmet kjøre igjen? (J/N): ")
	if svar.upper() == "J":
		i=0
	else:
		i=1