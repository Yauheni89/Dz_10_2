import pytest

from src.widget import get_data, mask_bank_data


# Фикстуры для тестовых данных
@pytest.fixture
def bank_data_samples():
    return [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("MasterCard 5555666677778888", "MasterCard 5555 66** **** 8888"),
    ]


@pytest.fixture
def date_samples():
    return [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ]


# Тесты для функции mask_bank_data
@pytest.mark.parametrize(
    "bank_data, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("MasterCard 5555666677778888", "MasterCard 5555 66** **** 8888"),
    ],
)
def test_mask_bank_data(bank_data, expected):
    assert mask_bank_data(bank_data) == expected


# Дополнительные тесты с использованием фикстуры
def test_mask_bank_data_with_fixture(bank_data_samples):
    for bank_data, expected in bank_data_samples:
        assert mask_bank_data(bank_data) == expected


# Тесты для функции get_data
@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ],
)
def test_get_data(date_string, expected):
    assert get_data(date_string) == expected
