import json
import logging
import os

import pandas as pd

# Определяем путь до корня проекта
root_directory = os.path.dirname(os.path.dirname(__file__))
log_directory = os.path.join(root_directory, "logs")

# Проверка и создание директории для логов, если она не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logging.basicConfig(
    filename=os.path.join(log_directory, "utils.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",  # Перезапись файла при каждом запуске
)

logger = logging.getLogger("utils")


def read_operations(file_path):
    """
    Читает данные о финансовых операциях из JSON-файла.

    Аргументы:
    file_path (str): Путь до JSON-файла с данными о финансовых операциях.

    Возвращает:
    list: Список словарей с данными о финансовых операциях.
    Если файл пустой, содержит не список или не найден,
    возвращается пустой список.
    """
    logger.debug(f"Операции чтения из файла: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Успешное чтение операций: {data}")
                return data
            else:
                logger.warning(f"Данные не являются списком: {data}")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON из файла: {file_path}")
        return []


def read_csv_transactions(file_path):
    transactions = []
    try:
        df = pd.read_csv(file_path, delimiter=";")
        for index, row in df.iterrows():
            transaction = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],  # Оставляем amount как строку
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "from": row["from"],
                "to": row["to"],
                "description": row["description"],
            }
            transactions.append(transaction)
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"Пустой CSV файл: {file_path}")
        return []
    except pd.errors.ParserError as e:
        print(f"Ошибка парсинга CSV файла: {file_path}. Ошибка: {e}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {file_path}. Ошибка: {e}")
        return []


def read_xlsx_transactions(file_name: str) -> list[dict]:
    """
    Читает данные о финансовых операциях из XLSX-файла и преобразовывает в список словарей.

    Аргументы:
    file_name (str): Путь до XLSX-файла с данными о финансовых операциях.

    Возвращает:
    list[dict]: Список словарей с данными о финансовых операциях.
    """
    try:
        df = pd.read_excel(file_name)

        result = df.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        ).tolist()

        return result

    except FileNotFoundError:
        print(f"Файл не найден: {file_name}")
        return []
    except pd.errors.EmptyDataError:
        print(f"Пустой XLSX файл: {file_name}")
        return []
    except pd.errors.ParserError as e:
        print(f"Ошибка парсинга XLSX файла: {file_name}. Ошибка: {e}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении XLSX файла: {file_name}. Ошибка: {e}")
        return []
