def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = [3, 7, 6, 10, 5]
tulos = laske_summa(lista)
print("Listan lukujen summa on:", tulos)
