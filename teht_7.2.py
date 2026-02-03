nimet = ()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break
    elif nimi not in nimet:
        nimet = nimet + (nimi,)
        print("Uusi nimi")
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")