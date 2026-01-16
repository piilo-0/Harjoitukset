leivi = float(input("Anna Leiviskät: "))
naul = float(input("Anna Naulat: "))
luod = float(input("Anna Luodit: "))

leivi_grammat = leivi * 20 * 32 * 13.3
naul_grammat = naul * 32 * 13.3
luod_grammat = luod * 13.3

Yht = leivi_grammat + naul_grammat + luod_grammat

kilogrammat = int(Yht // 1000)
grammat = Yht % 1000

print(f"Massa on {kilogrammat} kg ja {grammat:.2f} g.")