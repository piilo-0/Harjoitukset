class Hissi:
    def __init__(self, Alin, Ylin):
        self.Alin = Alin
        self.Ylin = Ylin
        self.Kerros = Alin

    def siirry_kerrokseen(self, kerros):
        if kerros < self.Kerros:
            while self.Kerros != kerros:
                self.kerros_alas()
        if kerros > self.Kerros:
            while self.Kerros != kerros:
                self.kerros_ylös()

    def kerros_ylös(self):
        if (self.Kerros < self.Ylin):
            self.Kerros += 1
        
    def kerros_alas(self):
        if (self.Kerros > self.Alin):
            self.Kerros -= 1

h = Hissi(1, 5)
h.siirry_kerrokseen(5)
print(h.Kerros)