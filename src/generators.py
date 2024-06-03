from typing import Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует операции по заданной валюте.

    :param transactions: Список словарей с банковскими операциями.
    :param currency: Код валюты для фильтрации.
    :return: Итератор, который возвращает операции в заданной валюте.
    """
    return (t for t in transactions if t["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описание каждой операции по очереди.

    :param transactions: Список словарей с банковскими операциями.
    :return: Итератор, который возвращает описание каждой операции.
    """
    return (t["description"] for t in transactions)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    :param start: Начальный номер диапазона (включительно).
    :param end: Конечный номер диапазона (включительно).
    :return: Генератор, который возвращает номера карт.
    """
    for number in range(start, end + 1):
        num_str = str(number)
        num_str = "0" * (16 - len(num_str)) + num_str
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
