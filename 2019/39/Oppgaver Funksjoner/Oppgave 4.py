tall_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def gjennomsnitt(tall_liste):
	summer = 0
	for nummer in tall_liste:
		summer = summer + nummer
	return summer/len(tall_liste)

print(gjennomsnitt(tall_liste))