tid = int(input("Skriv inn et (stort) antall sekunder - "))
aar = tid // (365 * 24 * 3600)
tid = tid % (365 * 24 *3600)
uker = tid // (7 * 24 * 3600)
tid = tid % (7 * 24 * 3600)
dager = tid // (24 * 3600)
tid = tid % (24 * 3600)
timer = tid // 3600
tid %= 3600
minutter = tid // 60
tid %= 60
sekunder = tid

print("Det blir = ", aar, "År,", uker, "Uker,", dager, "Dager,", timer, "Timer,", minutter, "Minutter og", sekunder, "Sekunder")