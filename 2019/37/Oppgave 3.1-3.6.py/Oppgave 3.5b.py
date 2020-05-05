# a) Lag et program som regner ut funksjonsverdien 𝑃(𝑥)=𝑥^4−5𝑥^2+4 for en verdi 𝑥_0 gitt av brukeren. 
# Programmet skal skrive ut en melding om (𝑥−𝑥_0) er en faktor i 𝑃(𝑥), eller ikke.

fortsett = 0

svar_liste = []

while fortsett < 1:

	def finn_faktoren():
		x = int(input("Skriv inn en x-verdi: "))
		
		if (x > 0):
			if (x**4 - 5*x**2 + 4 == 0):
				print("\n(x-" + str(x) + ") er en faktor")
				svar_liste.append(x)
				print("Riktige faktorer", svar_liste, "\n")
			else:
				print("\n(x-" + str(x) + ") er ikke en faktor")
				print("Riktige faktorer", svar_liste, "\n")
		else:
			if (x**4 - 5*x**2 + 4 == 0):
				print("\n(x+" + str(abs(x)) + ") er en faktor")
				svar_liste.append(x)
				print("Riktige faktorer", svar_liste, "\n")
			else:
				print("\n(x+" + str(abs(x)) + ") er ikke en faktor")
				print("Riktige faktorer", svar_liste, "\n")
		return

	fasit_liste = [-2, -1, 1, 2]
	fasit = all(item in svar_liste for item in fasit_liste)
	if fasit:
		print("\nDet faktoriserte utrykket er \nP(x)=(x-2)(x-1)(x+1)(x+2)\n")
		svar = input("Trykk på enter for å avslutte\n\n")
		fortsett = 1
	else:
		finn_faktoren()