from unittest.mock import mock_open, patch
from src.utils import read_operations


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
