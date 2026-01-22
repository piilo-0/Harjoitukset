kanta = float(input("Suorakulmion kanta: "))
korkeus = float(input("Suorakulmion korkeus: "))

pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print(f"Suorakulmion pinta-ala on: {pinta_ala:.2f}")
print(f"Suorakulmion piiri on: {piiri:.2f}")
