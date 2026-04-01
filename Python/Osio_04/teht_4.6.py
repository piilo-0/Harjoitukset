import random

yht_pist = int(input("Anna arvottavien pisteiden määrä: "))

pist = 0

i = 0
while i != yht_pist:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        pist += 1
    i += 1

pist_approx = 4 * pist / yht_pist

print(f"Piin likiarvo {yht_pist} satunnaispisteellä on: {pist_approx}")