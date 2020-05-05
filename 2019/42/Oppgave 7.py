telf_nummer = input("Skriv inn et telefonnummer: ")

if len(telf_nummer) == 8:
    print("Nummeret", telf_nummer, "er et gyldig telefonnummer!")
elif telf_nummer == "110" or telf_nummer == "112" or telf_nummer == "113": # hvis nummeret er et nødnummer
    print("Nummeret", telf_nummer, "er et gyldig nødnummer!")
elif len(telf_nummer) < 8:
    print("Nummeret", telf_nummer, "er ikke gyldig, det er for kort")
elif len(telf_nummer) > 8:
    print("Nummeret", telf_nummer, "er ikke gyldig, det er for langt")