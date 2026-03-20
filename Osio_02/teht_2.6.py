import random
kolmnumero = "".join(str(random.randint(0, 9)) for _ in range(3))
nelnumero = "".join(str(random.randint(1, 6)) for _ in range(4))

print(f"Kolminumeroinen koodi (0-9): {kolmnumero}")
print(f"Nelinumeroinen koodi (1-6): {nelnumero}")