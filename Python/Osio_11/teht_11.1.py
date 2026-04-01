class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumr):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumr

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumäärä)

class lehti(julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.päätoimittaja = toimittaja

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
        print("Päätoimittaja:", self.päätoimittaja)


aku_ankka = lehti("Aku Ankka", "Aki Hyyppä")
hytti = kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti.tulosta_tiedot()