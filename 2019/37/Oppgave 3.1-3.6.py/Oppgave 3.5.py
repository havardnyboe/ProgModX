# a) Lag et program som regner ut funksjonsverdien 𝑃(𝑥)=𝑥^4−5𝑥^2+4 for en verdi 𝑥_0 gitt av brukeren. 
# Programmet skal skrive ut en melding om (𝑥−𝑥_0) er en faktor i 𝑃(𝑥), eller ikke.

i = 0

while i<1:
	x = int(input("Skriv inn en x-verdi: "))
	if (x > 0):
		if (x**4 - 5*x**2 + 4 == 0):
			print("(x-" + str(x) + ") er en faktor")
			i = 1
		else:
			print("(x-" + str(x) + ") er ikke en faktor")
	else:
		if (x**4 - 5*x**2 + 4 == 0):
			print("(x+" + str(abs(x)) + ") er en faktor")
			i = 1
		else:
			print("(x+" + str(abs(x)) + ") er ikke en faktor")
