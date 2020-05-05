print(" \n ")
spiller_navn = input("Hva er navnet ditt?: ")
print(" \n ")

print("Velkommen " + spiller_navn + "! \n\nDu har havnet i en mørk og dyp skog, og forann deg ser du en sti. \nVil du følge stien, eller bli værende der du er? \n ")

valg1 = input('Skriv "bli værende" for å bli, eller "gå videre" for å følge stien \n\n - ')
if valg1.upper() == "BLI VÆRENDE":
	print("\n\nDu valgte å bli værende. \nDu venter, og venter, og venter. \nTil slutt har du ventet så lenge at kroppen din har begynt å spise seg selv opp. \n\n\n ------------------- \n\n   ***GAME OVER*** \n\n ------------------- \n\n\n")
elif valg1.upper() == "GÅ VIDERE":
	print("\n\nDu var klok og valgte å gå videre. \nEtter en stund kommer du fram til en kiste. \nDen har en kjetting hengende ut fra siden som preker mot deg. \nVil du åpne kisten, eller følge stien videre? \n")
	valg2 = input('Skriv "åpne kisten" for å åpne kisten, eller "gå videre" for å gå videre \n\n - ')
	if valg2.upper() == "ÅPNE KISTEN":
		print("\n\nDu valgte å åpne kisten, det viste seg at det derimot ikke var en kiste men en Mimic! \nMimicen spiste deg opp og la seg ned igjen for å sove. \n\n\n ------------------ \n\n   ***YOU DIED*** \n\n ------------------ \n\n\n")
		input("Tr")
	elif valg2.upper() == "GÅ VIDERE":
		print("\n\nDu valgte og gå videre.\nDet var klokt for foran deg så du et lys i enden av skogen.\nDu gikk mot lyset og kom deg ut av skogen \n\n\n ------------------- \n\n   ***VICTORY*** \n\n ------------------- \n\n\n")
	else:
		print("Du skrev inn noe ugyldig, start spillet på nytt!")
else:
	print("Du skrev inn noe ugyldig, start spillet på nytt!")