import random

rand_tall = random.randint(1,10) # genererer et tilfeldig tall mellom 1 og 10
br_tall = int(input("Skriv inn et tall mellom 1 og 100: "))
produkt = rand_tall*br_tall

print("\nProduktet av tallene er", produkt)
br_gjett = int(input("Hva tror du tallet er?: "))

print("\nDu gjettet {} og tallet var {}".format(br_tall, rand_tall))
if br_gjett == rand_tall: # hvis tallet brukeren gjetter er lik det tilfeldige tallet
    print("Du gjettet riktig!\n")
else:
    print("Du gjettet feil!\n")