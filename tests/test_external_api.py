from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_response = mock_get.return_value
    expected_result = 7345.12
    mock_response.json.return_value = {"result": expected_result}
    mock_response.status_code = 200

    result = convert_to_rub(100, "USD")
    assert result == expected_result


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    mock_response = mock_get.return_value
    expected_result = 8543.23
    mock_response.json.return_value = {"result": expected_result}
    mock_response.status_code = 200

    result = convert_to_rub(100, "EUR")
    assert result == expected_result


def test_convert_to_rub_rub():
    result = convert_to_rub(100, "RUB")
    assert result == 100.0
