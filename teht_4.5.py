oikeatunnus = "python"
oikeasalasana = "rules"

kierros = 0

while True:
    kierros += 1
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa")
        break
    if kierros == 5:
        print("Pääsy evätty")
        break
