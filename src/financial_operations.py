import re
from typing import List, Dict


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
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1
                break
    return category_count
