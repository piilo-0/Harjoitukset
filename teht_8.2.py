import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Tos1Hyv4Sa1asana",
    autocommit=True
)

iso = input("Anna maakoodi: ").upper()
kursori = yhteys.cursor()

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
"""

kursori.execute(sql, (iso,))
tulokset = kursori.fetchall()

if tulokset:
    print(f"Lentokentät maassa {iso}:")
    for tyyppi, maara in tulokset:
        print(f"{tyyppi}: {maara} kpl")
else:
    print("Maasta ei löytynyt lentokenttiä.")

kursori.close()
yhteys.close()
