import sys
import os
from unittest.mock import patch
from pervi import get_weather

API_KEY = "62cd1b130ee3aa244b201f453665bce0"

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


@patch("pervi.requests.get")
def test_get_weather_city_not_found(mock_get):
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}
    result = get_weather("НеверныйГород", API_KEY)
    assert "ошибка" in result
    assert result["ошибка"] == "Город не найден"


@patch("pervi.requests.get")
def test_get_weather_invalid_key(mock_get):
    mock_get.return_value.status_code = 401
    mock_get.return_value.json.return_value = {}
    result = get_weather("Almaty", "wrong_key")
    assert "ошибка" in result
    assert result["ошибка"] == "Неверный API-ключ"
