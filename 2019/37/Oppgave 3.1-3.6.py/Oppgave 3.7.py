#Lag et program som løser andregradslikningen 𝑎𝑥^2+𝑏𝑥+𝑐=0, ved å ta 𝑎,𝑏 𝑜𝑔 𝑐 som input.

a = float(input("Skriv inn en verdi for a: "))
b = float(input("Skriv inn en verdi for b: "))
c = float(input("Skriv inn en verdi for c: "))

if (b**2) - (4*a*c) == 0:
	en_losning = -b/(2*a)
	print(en_losning)
elif (b**2 - 4*a*c) > 0: 
	x_1 = (-b + (b**2 + 4*a*c)**(1/2))/(2*a)
	x_2 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
	print(x_1, "V", x_2)
else:
	print("Likningen har ingen løsning")
