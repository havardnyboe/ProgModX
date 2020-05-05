import random

fortsett = True
br_vinn = 0
pc_vinn = 0

while fortsett:
	# funksjon som definerer utfallet til pc-en
	def pc_utfall(tall):
		if tall == 1:
			utfall = "Stein"
		if tall == 2:
			utfall = "Saks"
		if tall == 3:
			utfall = "Papir"
		return utfall

	# funksjon som kjører programmet på nytt
	def kjor_prog_igjen():
		kjor_igjen = input("\nVil du kjøre programmet igjen? (J/N): ")
		if kjor_igjen.upper() == "J":
			fortsett = True
		else:
			fortsett = False
		return fortsett

	# funksjon som avslutter programmet og viser resultatet
	def avslutt(fortsett):
		if fortsett == False:
			print("\nDu vant {} ganger. PC-en vant {} ganger.\n".format(br_vinn, pc_vinn))
			input("-----Trykk på Enter for å avslutte-----")
		else:
			print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

	rand_tall = random.randint(1, 3)
	pc_utfall = pc_utfall(rand_tall) # finner utfallet til pc-en
	br_utfall = input("Stein, saks eller papir?\n\nSvar: ") # finner utfallet til brukeren

	print("\nPc-en valgte {}. Du valgte {}".format(pc_utfall.lower(), br_utfall.lower()))

	# finner ut hvem som har vunnet
	if br_utfall.upper() == "STEIN" and pc_utfall.upper() == "SAKS":
		print("Stein knuser saks, du vant!")
		br_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == "STEIN" and pc_utfall.upper() == "PAPIR":
		print("Papir dekker stein, du tapte!")
		pc_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == "SAKS" and pc_utfall.upper() == "STEIN":
		print("Stein knuser saks, du tapte!")
		pc_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == "SAKS" and pc_utfall.upper() == "PAPIR":
		print("Saks klipper papir, du vant!")
		br_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == "PAPIR" and pc_utfall.upper() == "STEIN":
		print("Papir dekker stein, du vant!")
		br_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == "PAPIR" and pc_utfall.upper() == "SAKS":
		print("Saks klipper papir, du tapte!")
		pc_vinn += 1
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	elif br_utfall.upper() == pc_utfall.upper():
		print("Dere valgte likt. Det ble ingen vinner.")
		fortsett = kjor_prog_igjen()
		avslutt(fortsett)

	# kjører programmet på nytt hvis man skriver noe annet enn 'Stein', 'Saks' eller 'Papir'
	else:
		print("Du skrev inn noe ugyldig, prøv igjen\n")
		fortsett = 0