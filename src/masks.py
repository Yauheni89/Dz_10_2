import logging

# Настройка логирования
logging.basicConfig(
    filename='logs/masks.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger('masks')


def mask_card_numbers(nums: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.debug(f"Получение замаскированного номера для: {nums}")
    masked = f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"
    logger.debug(f"Получение замаскированного номера для: {masked}")
    return masked


def mask_account_numbers(nums: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.debug(f"Маскировка номера счета: {nums}")
    masked = f"**{nums[-4:]}"
    logger.debug(f"Маскировка номера счета: {masked}")
    return masked


def get_masked_nums(nums: int | str) -> str:
    """Функция определяет введен номер карты или номер счета."""
    logger.debug(f"Получение замаскированного номера для: {nums}")
    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        return mask_card_numbers(nums)
    elif len(nums) == 20 and nums.isdigit():
        return mask_account_numbers(nums)
    else:
        logger.warning(f"Неверный входной номер: {nums}")
        return "Введите 16 или 20-значное число"
