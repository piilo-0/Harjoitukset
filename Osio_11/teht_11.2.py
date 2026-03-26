class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.Rekkari = rekkari
        self.Huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"Rekisterinumero: {self.Rekkari}")
        print(f"Huippunopeus   : {self.Huippunopeus} KM/H")
        print(f"Nopeus         : {self.nopeus}")
        print(f"Matka          : {self.matka}")

    def kiihdyta(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos

        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.Huippunopeus:
            self.nopeus = self.Huippunopeus

    def kulje(self, aika):
        self.matka += self.nopeus * aika

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akku):
        super().__init__(rekkari, huippunopeus)
        self.akku = akku


class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, bensa):
        super().__init__(rekkari, huippunopeus)
        self.bensa = bensa


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(120)
polttomoottoriauto.kiihdyta(100)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittarilukema: {sahkoauto.matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.matka} km")