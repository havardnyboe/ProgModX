tall_liste = [1, 2, 3, 4, 5, 6, 7, 8]

def get_partall(liste):
	partall_liste = []
	for tall in liste:
		if tall%2==0:
			partall_liste.append(tall)
	return partall_liste

print(get_partall(tall_liste))