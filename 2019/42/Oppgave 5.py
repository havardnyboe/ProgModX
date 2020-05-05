from random import randint


a = randint(1, 10)
b = randint(1, 10)

if a > b:
    print(a, "er størst")
elif a < b:
    print(b, "er størst")
else:
    print(a, "og", b, "er like store")

print("Tallene var {} og {}".format(a, b))