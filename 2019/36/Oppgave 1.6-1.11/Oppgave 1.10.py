benPerMil = float(input("Skriv inn bensinforbruket per mil            - "))
antKm = int(input("Skriv inn antall Km du skal kjøre            - "))
snittFart = int(input("Skriv inn gjennomsnittsfart for turen i km/t - "))

tidMin = (antKm / snittFart) * 60
literBen = benPerMil * (antKm/10)

print("Turen vil ta", int(round(tidMin, 0)), "minutter, og bilen vil bruke", float(round(literBen, 2)), "liter bensin")