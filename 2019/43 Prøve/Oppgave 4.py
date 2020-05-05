# a)
print("a)")
oddetall = 0
for i in range(101):
    if i % 2 == 1: # hvis resten blir 1 når det deles på 2
        oddetall += i
print(oddetall)

# b)
print("\nb)")
partall = 0
tall = 0
while tall <= 100:
    if tall % 2 == 0: # hvis resten blir 0 når det deles på 2
        partall += tall 
    tall += 1
print(partall)
