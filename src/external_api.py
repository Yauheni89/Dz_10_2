import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(amount, currency_code):
    """
        Конвертирует заданную сумму из указанной валюты в рубли.

        Аргументы:
        amount (float): Сумма для конвертации.
        currency_code (str): Код валюты, из которой происходит конвертация. Например, "USD", "EUR", "GBP" и т.д.

        Возвращает:
        float: Сумма в рублях после конвертации.

        Исключения:
        ValueError: Если возникает ошибка при конвертации валюты
        или в ответе от сервера не содержится ожидаемый результат.
        """
    if currency_code == "RUB":
        return float(amount)

    params = {"from": currency_code, "to": "RUB", "amount": amount}

    headers = {"apikey": API_KEY}

    response = requests.get(BASE_URL, headers=headers, params=params)
    response_data = response.json()

    if response.status_code == 200 and "result" in response_data:
        return response_data["result"]
    else:
        raise ValueError("Ошибка при конвертации валюты")
