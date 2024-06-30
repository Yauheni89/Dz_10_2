import re
from typing import Dict, List
from collections import Counter


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует транзакции по строке поиска в описании.

    :param transactions: Список словарей с банковскими операциями.
    :param search_string: Строка поиска.
    :return: Список транзакций, в описании которых содержится строка поиска.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    :param transactions: Список словарей с банковскими операциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь, где ключи - категории, значения - количество операций в каждой категории.
    """
    category_counter = Counter(transaction['category'] for transaction in transactions if transaction.get('category') in categories)
    return dict(category_counter)
