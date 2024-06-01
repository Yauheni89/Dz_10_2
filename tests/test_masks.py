import pytest

from src.masks import get_masked_nums, mask_account_numbers, mask_card_numbers


# Фикстуры для тестовых данных
@pytest.fixture
def card_numbers():
    return [
        "1234567890123456",
        "1111222233334444",
        "5555666677778888"
    ]


@pytest.fixture
def account_numbers():
    return [
        "12345678901234567890",
        "11112222333344445555",
        "98765432109876543210"
    ]


# Тесты для функции mask_card_numbers
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("5555666677778888", "5555 66** **** 8888"),
])
def test_mask_card_numbers(card_number, expected):
    assert mask_card_numbers(card_number) == expected


# Тесты для функции mask_account_numbers
@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("11112222333344445555", "**5555"),
    ("98765432109876543210", "**3210"),
])
def test_mask_account_numbers(account_number, expected):
    assert mask_account_numbers(account_number) == expected


# Тесты для функции get_masked_nums
@pytest.mark.parametrize("number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("12345678901234567890", "**7890"),
    ("1234", "Введите 16 или 20-значное число"),
    ("abcd1234567890123456", "Введите 16 или 20-значное число"),
])
def test_get_masked_nums(number, expected):
    assert get_masked_nums(number) == expected
