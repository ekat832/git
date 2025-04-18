import requests


def get_weather(city: str, api_key: str) -> dict:
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?q={city}"
            f"&appid={api_key}&units=metric&lang=ru"
        )
        response = requests.get(url)
        data = response.json()

        if response.status_code == 401:
            return {"ошибка": "Неверный API-ключ"}
        elif response.status_code == 404:
            return {"ошибка": "Город не найден"}
        elif response.status_code != 200:
            return {"ошибка": "Ошибка сервера"}

        return {
            "город": data["name"],
            "температура": data["main"]["temp"],
            "описание": data["weather"][0]["description"]
        }

    except requests.exceptions.RequestException:
        return {"ошибка": "Проблема с подключением"}
