import random
from xml.sax.saxutils import prepare_input_source

luku = random.randint(1, 10)

while True:
    syote = int(input("Arvaa luku 1-10: "))
    if syote == luku:
        print("Oikein!")
        break
    if syote > luku:
        print("Liian suuri arvaus!")
    if syote < luku:
        print("Liian pieni arvaus!")