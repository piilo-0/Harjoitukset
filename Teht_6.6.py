import math

def yksikkohinta(halkaisija, hinta):
    m = (halkaisija / 2) / 100
    ala = math.pi * m ** 2
    return hinta / ala

print("Pizza 1:")
halkaisija1 = float(input("Anna halkaisija senttimetreinä: "))
hinta1 = float(input("Anna hinta euroina: "))

print("\nPizza 2:")
halkaisija2 = float(input("Anna halkaisija senttimetreinä: "))
hinta2 = float(input("Anna hinta euroina: "))

yh1 = yksikkohinta(halkaisija1, hinta1)
yh2 = yksikkohinta(halkaisija2, hinta2)

print(f"\nPizza 1 yksikköhinta: {yh1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {yh2:.2f} €/m²")

if yh1 < yh2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yh2 < yh1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä edullisia.")
