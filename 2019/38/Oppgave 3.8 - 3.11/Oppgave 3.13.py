slutt = 0

while slutt < 1:
		
	fib = [0, 1]
	til_nummer = int(input("\nHvor mange tall vil du se i fibonaccifølgen?: "))
	
	for nummer in range(1, til_nummer):
		nytt_nummer = fib[-1]+fib[-2]
		fib.append(nytt_nummer)
	
	fib.pop(0)
	if til_nummer > 0:
		print(fib)
	else:
		print("\nDu skrev inn et ugyldig tall, prøv igjen")

	svar = input("\nSkal programmet kjøre igjen? (J/N): ")
	if svar.upper() == "J":
		print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		slutt=0
	else:
		slutt=1