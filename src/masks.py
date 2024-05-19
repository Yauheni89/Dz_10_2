def mask_card_numbers(nums: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    return f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_account_numbers(nums: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"**{nums[-4:]}"


def get_masked_nums(nums: int | str) -> str:
    """Функция определяет введен номер карты или номер счета."""

    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        return mask_account_numbers(nums)

    else:
        return "Введите 16 или 20-значное число"
