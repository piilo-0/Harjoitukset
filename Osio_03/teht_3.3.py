sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")
else:
    print("Tuntematon sukupuoli. Anna 'nainen' tai 'mies'.")