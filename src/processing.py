def filter_by_state(transactions: object, state: object = "EXECUTED") -> object:
    """Функция принимает на вход список словарей и значение для ключа stat
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает
     новый список, содержащий только те словари, у которых ключ state
     содержит переданное в функцию значение."""
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            filtered_transactions.append(transaction)
    return filtered_transactions
