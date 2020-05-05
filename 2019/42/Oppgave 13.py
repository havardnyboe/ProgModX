saldo = float(input("Hva er saldeon på kontoen din?: "))
budsjett = float(input("Hvor stort er budsjettet ditt for ferien?: "))
tot_forbruk = 0
for dager in range(14):
    forbruk = float(input("Hva var forbruket ditt for dag nr. {}?: ".format(dager+1)))
    tot_forbruk += forbruk
    if tot_forbruk >= budsjett or forbruk >= budsjett:
        print("\nDu har overskredet budsjettet ditt!")
        break
    else:
        continue
saldo -= tot_forbruk
print("\nDitt totale forbruk for ferien var {} kr\n".format(tot_forbruk))