import requests


paikka = input("Anna paikkakunnan nimi:")

request = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&units=metric&appid=be39535216ed32f2366b034f4f8cce5a"

vastaus = requests.get(request).json()

print(f"Paikan {paikka} Sääksi palautui: {vastaus['weather'][0]['main']}")
print(f"Paikan {paikka} Lämpötilaksi palautui: {vastaus['main']['temp']} celcius astetta")