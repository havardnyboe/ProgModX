# a) Lag et program som regner ut funksjonsverdien 𝑃(𝑥)=𝑥^4−5𝑥^2+4 for en verdi 𝑥_0 gitt av brukeren. 
# Programmet skal skrive ut en melding om (𝑥−𝑥_0) er en faktor i 𝑃(𝑥), eller ikke.

# b) Utvid programmet slik at du kan fortsette å taste inn flere verdier for 𝑥_0, helt til du har funnet alle de fire lineære faktorene. 
# Skriv så ut det faktoriserte polynomet.

range_start = int(input("Skriv inn en startverdi: "))
range_slutt = int(input("Skriv inn en sluttverdi: "))

fasit_liste = []

for x in range(range_start, range_slutt+1):
	if (x > 0):
		if (x**4 - 5*x**2 + 4 == 0):
			print("(x-" + str(x) + ") er en faktor")
			fasit_liste.append(x)
	else:
		if (x**4 - 5*x**2 + 4 == 0):
			print("(x+" + str(abs(x)) + ") er en faktor")
			fasit_liste.append(x)

if fasit_liste == [-2, -1, 1, 2]:
	print("Funksjonen blir: \n P(X)=(x-2)(x-1)(x+1)(x+2)")
else:
	print("En eller flere faktorer mangler, prøv igjen!")
