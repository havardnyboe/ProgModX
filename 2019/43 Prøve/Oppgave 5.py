import random

kortstokk = []
farge = ""
kjor = True
kort_igjen = 52
# Lager kortstokken 
for i in range(1, 53):
    kortstokk.append(i)

def trekk_kort():
    rand_kort_index = random.randint(0, len(kortstokk)-1) # velger et kort (index i listen)
    rand_kort = kortstokk[rand_kort_index] # tilordner "rand_kort" verdien til kortet
    kortstokk.pop(rand_kort_index) # fjerner kortet fra kortstokken
    # tildeler riktig farge til kortet
    if rand_kort >= 0 and rand_kort <=13:
        farge = "Hjerter"
    if rand_kort >= 14 and rand_kort <=26:
        farge = "Spar"
        rand_kort = rand_kort - 13
    if rand_kort >= 27 and rand_kort <=39:
        farge = "Ruter"
        rand_kort = rand_kort - 26
    if rand_kort >= 40 and rand_kort <=52:
        farge = "Kløver"
        rand_kort = rand_kort - 39
    # Sjekker om kortet er et honørkort
    if rand_kort == 1: # Ess
        rand_kort = "{} Ess".format(farge)
        return rand_kort
    if rand_kort == 11: # Knekt
        rand_kort = "{} Knekt".format(farge)
        return rand_kort
    if rand_kort == 12: # Dame
        rand_kort = "{} Dame".format(farge)
        return rand_kort
    if rand_kort == 13: # Konge
        rand_kort = "{} Konge".format(farge)
        return rand_kort
    rand_kort = "{} {}".format(farge, rand_kort)
    return rand_kort
# kjører programmet til brukeren ikke vil mer eller til bunken er tom
while kjor:
    print("\nDu trakk {}".format(trekk_kort()))
    kort_igjen -= 1
    print("Det er {} kort igjen\n".format(kort_igjen))
    kjor_igjen = input("Vil du trekke et kort til (J/N): ")
    if kort_igjen == 0: # hvis kortsokken er tom
        print("\nKortstokken er tom\n")
        kjor = False
    else:
        if kjor_igjen.upper() == "J" or kjor_igjen.upper() == "JA":
            kjor = True
        else: 
            kjor = False
        