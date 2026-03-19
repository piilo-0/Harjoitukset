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


autot = []

for i in range(1, 11):
    rekkari = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekkari, huippunopeus)
    autot.append(auto)

kilpailu = True

while kilpailu:
    for auto in autot:
        nopeudenmuutos = random.randint(-10, 15)
        auto.kiihdyta(nopeudenmuutos)
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu = False

print(f"{'Rekisteri':<12}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
print("-" * 47)

for auto in autot:
    print(f"{auto.Rekkari:<12}{auto.Huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10.1f}")