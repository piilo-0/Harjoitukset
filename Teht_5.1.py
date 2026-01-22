import random

kuutiot = int(input("Kuinka monta arpakuutiota heitetään?: "))
summa = 0

for i in range(kuutiot):
    luku = random.randint(1, 6)
    summa += luku
print(f"noppien summa oli {summa}")
