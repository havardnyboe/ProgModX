import random

fortsett_program = True

while fortsett_program:

	rand_tall = random.randint(1, 100)
	fortsett = True
	ant_forsøk = 0

	print("\nEt tilfeldig tall mellom 1 og 100 har blitt generet!\n")

	while fortsett:

		ant_forsøk += 1
		gjett_tall = int(input("Gjett tallet: "))

		if gjett_tall == rand_tall:
			print("\nGratulerer! Tallet du gjettet riktg tall på {} forsøk!\n".format(ant_forsøk))
			fortsett = False
			slutt_program = input("Vil du kjøre programmet igjen? (J/N): ")
			if slutt_program.upper() == "J":
				print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			else:
				fortsett_program = False
		elif gjett_tall < rand_tall:
			print("Tallet du gjettet er for lavt, gjett et høyere tall!\n")
		elif gjett_tall > rand_tall:
			print("Tallet du gjettet er for høyt, gjett et lavere tall!\n")