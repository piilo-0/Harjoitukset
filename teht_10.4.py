import random
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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeudenmuutos = random.randint(-10, 15)
            auto.kiihdyta(nopeudenmuutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.nimi}")
        print(f"{'Rekisteri':<12}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        print("-" * 47)

        for auto in self.autot:
            print(f"{auto.Rekkari:<12}{auto.Huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    rekkari = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekkari, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
