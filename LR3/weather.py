import requests
import LR3.ApiKey as key

def getWeather(apiKey, city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": apiKey, "lang": "ru", "units": "metric"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather = response.json()
        return weather
    else:
        print(f"Ошибка {response.status_code}: {response.text}")

def run():
    apiKey = key.getApiKey()
    city = "Saint Petersburg"
    weather = getWeather(apiKey, city)

    if weather:
        print(f"Погода в {city} {weather['coord']}")
        print(f"Температура: {weather['main']['temp']}°C")
        print(f"Прочее: {weather['weather'][0]['description']}")
    else:
        print("Где-то ошибочка вышла")
