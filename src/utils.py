import json


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
    try:
        # Открываем файл в режиме чтения с кодировкой 'utf-8'
        with open(file_path, "r", encoding="utf-8") as file:
            # Загружаем содержимое файла как JSON
            data = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        # Возвращаем пустой список в случае ошибки (файл не найден или ошибка при чтении JSON)
        return []
