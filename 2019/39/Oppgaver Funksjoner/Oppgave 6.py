def fibonacci(nummer):
	fib_liste = [0, 1]
	for i in range(nummer-1):
		nytt_nummer = fib_liste[-1]+fib_liste[-2]
		fib_liste.append(nytt_nummer)
		i = i+1

	return print("Tall nummer", i+1, "er", fib_liste[-1])

tall_nummer = int(input("Hvilket tall nummer vil du se i fibonaccifølgen?: "))
fibonacci(tall_nummer)