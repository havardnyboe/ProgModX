tall1 = int(input("Skriv inn et tall - "))
tall2 = int(input("Skriv inn et annet tall - "))

tallSum = tall1 + tall2
tallDiff = tall1 - tall2
tallProd = tall1 * tall2
tallForh = tall1 / tall2

print("Summen av tallene er", tallSum)
print("Differansen av tallene er", tallDiff)
print("Produktet av tallene er", tallProd)
print("Forholdet mellom tallene er", round(tallForh, 3))