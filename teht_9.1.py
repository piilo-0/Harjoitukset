class Auto:
    def __init__(self, Rekkari, Huippunopeus):
        self.Rekkari = Rekkari
        self.Huippunopeus = Huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"Rekisterinumero: {self.Rekkari}")
        print(f"Huippunopeus   : {self.Huippunopeus} KM/H")
        print(f"Nopeus         : {self.nopeus}")
        print(f"Matka          : {self.matka}")

Uusiauto = Auto("ABC-123", 142)

Uusiauto.tulosta_tiedot()
