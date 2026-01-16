import math

pintala: float
piiri: float

Kanta: float = float(input("Kolmion kanta: "))
Korkeus: float = float(input("Kolmion korkeus: "))

pintala = (Kanta * Korkeus) / 2

sivu = math.sqrt((Kanta / 2) ** 2 + Korkeus ** 2)
piiri = Kanta + 2 * sivu

print(f"Kolmion pinta-ala on: {pintala:.2f}")
print(f"Kolmion piiri on: {piiri:.2f}")
