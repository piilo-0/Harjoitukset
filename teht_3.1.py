koko = float(input("Anna kuhan koko senttimetreinä: "))

if koko >= 37:
    print(f"Kuha on hyvän kokoinen voit pitää sen.")
else:
    print(f"Kuha on alamittainen. Laske takaisin järveen")
    print(f"Kuha on {37 - koko:.1f} senttiä liian lyhyt")