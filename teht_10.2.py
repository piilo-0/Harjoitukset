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

    
class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = []

        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_numero, kerros):
        hissi = self.hissit[hissi_numero]
        hissi.siirry_kerrokseen(kerros)
        
talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(0, 1)
