import random

def kast_terning():
    print("Terningen viser: {}".format(random.randint(1,6)))

print("Trykk på Enter for å kaste terningen")

fortsett = True

while fortsett:
    if input() == "":
        kast_terning()
    else:
        fortsett = False