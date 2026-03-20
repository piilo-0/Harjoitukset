from math import inf

isoin: int = -inf
pienin: int = inf
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    if int(syote) > isoin:
        isoin = int(syote)
    if int(syote) < pienin:
        pienin = int(syote)
print(f"Isoin annetu luku oli {isoin} pienin oli {pienin}")