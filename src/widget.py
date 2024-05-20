from .masks import get_masked_nums


def mask_bank_data(bank_data: str) -> str:
    """Функция принимает данные и возвращает данные замаскированным номером карты/счета"""
    data_parts = bank_data.split()
    data_parts[-1] = get_masked_nums(data_parts[-1])
    return " ".join(data_parts)


def get_data(date_string: str) -> str:
    """Функция преобразует дату формата ГГГГ-ММ-ДД в формат ДД-ММ-ГГГГ."""
    date = date_string.split("T", 1)[0]
    formated_date_list = date.split("-")
    year, month, day = formated_date_list
    return f"{day}.{month}.{year}"
