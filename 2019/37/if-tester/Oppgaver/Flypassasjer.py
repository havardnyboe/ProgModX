#Lag et program som tar inn en flypassasjers fornavn, etternavn og kjønn.
#Hvis kjønnet er kvinne, skal man bruke tittelen "Mrs." Er ikke kjønnet kvinne, skal tittelen "Mr." brukes.

fornavn = input("Skriv inn fornavn:     ")
etternavn = input("Skriv inn etternavn:   ")
kjonn = input("Skriv inn kjønn (K/M): ")

if kjonn.upper() == "K":
	fornavn = "Mrs. " + fornavn
	print("Hei", fornavn, etternavn + "!")
elif kjonn.upper() == "M":
	fornavn = "Mr. " + fornavn
	print("Hei", fornavn, etternavn + "!")
else:
	print("Du skrev inn noe ugyldig, prøv igjen")