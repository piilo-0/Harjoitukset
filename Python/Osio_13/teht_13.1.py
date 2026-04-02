from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku < 2:
        return False
    if luku == 2:
        return True
    if luku % 2 == 0:
        return False

    jakaja = 3
    while jakaja * jakaja <= luku:
        if luku % jakaja == 0:
            return False
        jakaja += 2

    return True

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    return jsonify({
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    })

app.run(host="127.0.0.1", port=3000, debug=True)