# Lag et program som tar to tall som input. 
# Programmet skal finne det minste tallet og skrive ut dette.

tall1 = int(input("Skriv inn et tall: "))
tall2 = int(input("Skriv inn et tall: "))

if (tall1<tall2):
	print(tall1, "er mindre enn", tall2)
else:
	print(tall2, "er mindre enn", tall1)