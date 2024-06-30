import logging
import os

# Определяем путь до корня проекта
root_directory = os.path.dirname(os.path.dirname(__file__))
log_directory = os.path.join(root_directory, "logs")

# Проверка и создание директории для логов, если она не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logging.basicConfig(
    filename=os.path.join(log_directory, "masks.log"),
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="w",  # Перезапись файла при каждом запуске
)

logger = logging.getLogger("masks")


def mask_card_numbers(nums: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.debug(f"Номер маскировочной карты: {nums}")
    masked = f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"
    logger.debug(f"Номер маскировочной карты: {masked}")
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
