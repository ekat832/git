from pervi import get_weather

API_KEY = "62cd1b130ee3aa244b201f453665bce0"


def main():
    city = input("Город: ")
    result = get_weather(city, API_KEY)

    if "ошибка" in result:
        print("Ошибка:", result["ошибка"])
    else:
        print(
            f"Погода в {result['город']}: {result['температура']}°C, "
            f"{result['описание']}"
        )


if __name__ == "__main__":
    main()
