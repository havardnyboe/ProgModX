
ant_innsekter = 0

for dager in range(5):
    innsekter = int(input("Hvor mange insekter ble fanget den {}. dagen?: ".format(dager+1)))
    ant_innsekter += innsekter

print("\nDet ble fanget {} innsekter til sammen\n".format(ant_innsekter))