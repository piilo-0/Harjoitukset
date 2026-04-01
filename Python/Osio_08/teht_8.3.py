import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Tos1Hyv4Sa1asana",
    autocommit=True
)

kursori = yhteys.cursor()


icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentokentän ICAO-koodi: ").upper()


sql = """
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident = %s
"""

kursori.execute(sql, (icao1,))
kentta1 = kursori.fetchone()

kursori.execute(sql, (icao2,))
kentta2 = kursori.fetchone()

if kentta1 and kentta2:
    koord1 = (kentta1[0], kentta1[1])
    koord2 = (kentta2[0], kentta2[1])

    etaisyys = geodesic(koord1, koord2).kilometers

    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys:.2f} km.")
else:
    print("Toista tai molempia ICAO-koodeja ei löytynyt tietokannasta.")

kursori.close()
yhteys.close()
