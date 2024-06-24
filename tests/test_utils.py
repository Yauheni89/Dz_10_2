from unittest.mock import mock_open, patch

import pytest
from pandas import DataFrame

from src.utils import read_csv_transactions, read_operations, read_xlsx_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 441945886, "state": "EXECUTED"}]')
def test_read_operations_valid(mock_file):
    result = read_operations("data/operations.json")
    assert result == [{"id": 441945886, "state": "EXECUTED"}]


@patch("builtins.open", new_callable=mock_open, read_data='{"id": 441945886, "state": "EXECUTED"}')
def test_read_operations_invalid_format(mock_file):
    result = read_operations("data/operations.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_operations_empty_file(mock_file):
    result = read_operations("data/operations.json")
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_operations_file_not_found(mock_file):
    result = read_operations("data/operations.json")
    assert result == []


@pytest.fixture
def mock_read_csv_with_data():
    # Mock data for CSV file
    csv_data = DataFrame(
        {
            "id": [650703, 3598919, 593027],
            "state": ["EXECUTED", "EXECUTED", "CANCELED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
            "amount": [16210, 29740, 30368],
            "currency_name": ["Sol", "Peso", "Shilling"],
            "currency_code": ["PEN", "COP", "TZS"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
            "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
        }
    )
    with patch("src.utils.pd.read_csv", return_value=csv_data) as mock_read_csv:
        yield mock_read_csv, csv_data


@pytest.fixture
def mock_read_excel_with_data():
    # Mock data for XLSX file
    xlsx_data = DataFrame(
        {
            "id": [650703, 3598919, 593027],
            "state": ["EXECUTED", "EXECUTED", "CANCELED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
            "amount": [16210, 29740, 30368],
            "currency_name": ["Sol", "Peso", "Shilling"],
            "currency_code": ["PEN", "COP", "TZS"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
            "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
        }
    )
    with patch("src.utils.pd.read_excel", return_value=xlsx_data) as mock_read_excel:
        yield mock_read_excel, xlsx_data


def test_read_csv_transactions(mock_read_csv_with_data):
    mock_read_csv, csv_data = mock_read_csv_with_data
    result = read_csv_transactions("mock.csv")
    assert result == csv_data.to_dict(orient="records")


def test_read_csv_transactions_file_not_found():
    with patch("src.utils.pd.read_csv", side_effect=FileNotFoundError):
        result = read_csv_transactions("nonexistent.csv")
        assert result == []


def test_read_csv_transactions_empty_file():
    empty_data = DataFrame()
    with patch("src.utils.pd.read_csv", return_value=empty_data):
        result = read_csv_transactions("empty.csv")
        assert result == []


def test_read_csv_transactions_other_exception():
    with patch("src.utils.pd.read_csv", side_effect=Exception):
        result = read_csv_transactions("error.csv")
        assert result == []


def test_read_xlsx_transactions(mock_read_excel_with_data):
    mock_read_excel, xlsx_data = mock_read_excel_with_data
    result = read_xlsx_transactions("mock.xlsx")
    assert result == xlsx_data.to_dict(orient="records")


def test_read_xlsx_transactions_file_not_found():
    with patch("src.utils.pd.read_excel", side_effect=FileNotFoundError):
        result = read_xlsx_transactions("nonexistent.xlsx")
        assert result == []


def test_read_xlsx_transactions_empty_file():
    empty_data = DataFrame()
    with patch("src.utils.pd.read_excel", return_value=empty_data):
        result = read_xlsx_transactions("empty.xlsx")
        assert result == []


def test_read_xlsx_transactions_other_exception():
    with patch("src.utils.pd.read_excel", side_effect=Exception):
        result = read_xlsx_transactions("error.xlsx")
        assert result == []
