tall1 = float(input("Skriv inn et tall: "))
tall2 = float(input("Skriv inn et tall: "))
opperator = input("Velg opperator (+ - * /): ")

# pluss
if opperator == "+":
    print("\n{} + {} = ".format(tall1, tall2))
    print(round(tall1+tall2, 3))
# minus
if opperator == "-":
    print("\n{} - {} = ".format(tall1, tall2))
    print(round(tall1-tall2, 3))
# gange
if opperator == "*":
    print("\n{} * {} = ".format(tall1, tall2))
    print(round(tall1*tall2, 3))
# dele
if opperator == "/":
    print("\n{} / {} = ".format(tall1, tall2))
    print(round(tall1/tall2, 3))