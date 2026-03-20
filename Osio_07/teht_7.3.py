# Esitäytetty lentoasema
ICAO = {
    "EFHK": "Helsinki-Vantaa lentoasema"
}

while True:
    print("(1) Lisää lentoasema")
    print("(2) Etsi lentoasema")
    print("(3) Lopeta")

    option = input("Mitä haluat tehdä?: ")

    if option == "1":
        koodi = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        ICAO[koodi] = nimi
        print("Lentoasema tallennettu.")

    elif option == "2":
        koodi = input("Anna lentoaseman ICAO-koodi: ").upper()
        if koodi in ICAO:
            print(f"Lentoaseman nimi: {ICAO[koodi]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif option == "3":
        break

    else:
        print("Virheellinen valinta.")
