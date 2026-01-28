def gallon_L(gallonat):
    return gallonat * 3.785


while True:
    maara = float(input("Anna bensiinimäärä gallonina: "))

    if maara < 0:
        break

    litrat = gallon_L(maara)
    print(f"{maara} gallonia on {litrat:.3f} litraa")
