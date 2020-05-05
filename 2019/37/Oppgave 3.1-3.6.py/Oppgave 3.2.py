# Lag et program som tar et tall som input. 
# Programmet skal så vurdere og skrive ut om tallet er et positivt tall, et negativt tall eller null.

tall1 = int(input("Skriv inn et tall: "))

if (tall1 > 0):
	print("Tallet er positivt")
elif (tall1 == 0):
	print("Tallet er null")
else:
	print("Tallet er negativt")