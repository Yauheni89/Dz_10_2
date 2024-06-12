import os

import pytest

from src.decorators import log


# Тест для успешного выполнения функции
@log(filename="test_log.txt")
def add(x, y):
    return x + y


def test_add_success():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = add(1, 2)
    assert result == 3

    with open("test_log.txt") as f:
        for line in f:
            if "add ok" in line:
                break
        else:
            assert False, "Ожидаемое сообщение 'add ok' не найдено в файле журнала"


# Тест для ошибочного выполнения функции
@log(filename="test_log.txt")
def divide(x, y):
    return x / y


def test_divide_error():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(ZeroDivisionError):
        divide(4, 0)

    with open("test_log.txt") as f:
        for line in f:
            if "divide error:" in line and "Inputs: (4, 0)" in line:
                break
        else:
            assert False, "Ожидаемое сообщение 'divide error' не найдено в файле журнала"
