#Lag et programm som tester om et tall er et partall eller et oddetall

tall1 = int(input("Skriv inn et tall: "))

if tall1 % 2 == 0:
	print("Tallet er et partall!")
else:
	print("Taller er et oddetall!")