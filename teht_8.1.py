import mysql.connector

# Yhdistetään tietokantaan
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Tos1Hyv4Sa1asana",
    autocommit=True
)
icao = input("Anna lentoaseman ICAO-koodi: ").upper()

kursori = yhteys.cursor()

sql = """
SELECT name
FROM airport
WHERE ident = %s
"""

kursori.execute(sql, (icao,))
tulos = kursori.fetchone()

if tulos:
    print(f"Lentokentän nimi: {tulos[0]}")
else:
    print("ICAO-koodia vastaavaa lentokenttää ei löytynyt.")
kursori.close()
yhteys.close()
