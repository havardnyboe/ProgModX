#Oppgave 1.2
tall1 = 5
tall2 = 10

print(tall1, "ganger", tall2, "er", tall1*tall2)

#Oppgave 1.3
#a) Regnestykket blir ikke regnet ut fordi tallene leses som en string
#b)
a = 3.4 
b = 20.5
total = a*b
print(total)
print(int(total))

#Det blir printet to forskjellige tall fordi print(int(total)) runder ned tallet til et heltal

#Oppgave 1.4
fornavn = "Ola"
etternavn = "Nordmann"
domene = "bedrift.no"

epost = fornavn+"."+etternavn+"@"+domene

print(epost)
