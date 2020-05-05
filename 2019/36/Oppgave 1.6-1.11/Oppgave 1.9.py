forPris = float(input("Skriv inn prisen på varen - "))
rabattPros = float(input("Skriv inn rabatten (uten % tegnet) - "))

rabattKr = forPris * (rabattPros/100)
etterPris = forPris - rabattKr
print("Den nye prisen er", int(round(etterPris, 0)), "kr")