import sys
import requests

API_KEY = ""

URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        "lang" : "es",
        'units': 'metric'
    }

    respuesta = requests.get(URL, params=params)
    if respuesta.status_code != 200:
        print("Error al obtener los datos del clima: ", respuesta.json().get("message", "Error desconocido"))
        return
    
    datos = respuesta.json()
    print(f"\nClima en {city.title()}:") 
    print(f"Temperatura: {datos['main']['temp']}°C")
    print(f"Estado: {datos['weather'][0]['description']}")
    print(f"Humedad: {datos['main']['humidity']}%")
    print(f"Viento: {datos['wind']['speed']} m/s")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python clima.py <ciudad>")
    else:
        ciudad = " ".join(sys.argv[1:])
        get_weather(ciudad)
