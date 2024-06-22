import json
import logging
import os

# Определяем путь до корня проекта
root_directory = os.path.dirname(os.path.dirname(__file__))
log_directory = os.path.join(root_directory, 'logs')

# Проверка и создание директории для логов, если она не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logging.basicConfig(
    filename=os.path.join(log_directory, 'utils.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levellevelname)s - %(message)s',
    filemode='w'  # Перезапись файла при каждом запуске
)

logger = logging.getLogger('utils')


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
