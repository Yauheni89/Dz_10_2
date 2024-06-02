def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа stat
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает
     новый список, содержащий только те словари, у которых ключ state
     содержит переданное в функцию значение."""
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_dicts_by_date(dicts_list: list) -> list:
    """Функция принимает на вход список словарей и возвращает новый список, в котором
    исходные словари отсортированы по убыванию даты (ключ date)."""
    sorted_list = sorted(dicts_list, key=lambda x: x["date"], reverse=True)
    return sorted_list
