import json


def read_transactions(file_path):
    """
    Функция, которая читает данные о финансовых транзакциях из JSON-файла.

    Args:
        file_path (str): Путь до JSON-файла.

    Returns:
        list: Список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
