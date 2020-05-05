teller = 0

while teller < 1:
	fortsett = (input("Skriv inn et tall: "))
	def ukedager(dag_nummer):
		ukedager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']
		return ukedager[dag_nummer-1]

	if fortsett.upper() == "STOPP" or int(fortsett) > 7 or int(fortsett) < 1:
		teller = 1
	else:
		print(ukedager(int(fortsett)))