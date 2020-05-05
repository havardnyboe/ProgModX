#Oppg.3 Lag et program der du konverterer fra en datatype til en annen.

tall1 = "5"
print(tall1 + tall1, int(tall1) + int(tall1))

# Oppg.4

tall = 3
rest = tall % 2
if rest > 0:
    print("Tallet er ikke delelig med 2!")
elif rest == 0:
    print("Tallet er delelig med 2!")

# Oppg.5

tid = 4
strekning = 10
fart = strekning / tid
print(fart)