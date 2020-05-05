def fakultet(tall):
    if tall < 0:
        print("Tallet må være positivt!")
    else:
        tall_fakultet = 1
        for i in range(1, tall+1):
            tall_fakultet *= i
        return tall_fakultet

tall1 = int(input("Skriv inn et tall: "))
print("{}! = {}".format(tall1, fakultet(tall1)))