from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="Tos1Hyv4Sa1asana",
    autocommit=True
)

@app.route("/kenttä/<icao>", methods=["GET"])
def hae_kentta(icao):
    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """

    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
    else:
        vastaus = {
            "error": "ICAO-koodia ei löytynyt"
        }

    return jsonify(vastaus)

app.run(host="127.0.0.1", port=3000, debug=True)