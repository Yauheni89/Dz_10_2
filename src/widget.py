from .masks import get_masked_nums


def mask_bank_data(bank_data: str) -> str:
    """Функция принимает данные и возвращает данные замаскированным номером карты/счета"""
    data_parts = bank_data.split()

    data_parts[-1] = get_masked_nums(data_parts[-1])

    return " ".join(data_parts)
