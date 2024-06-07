import functools
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызова функции и её результата.

    Если `filename` задан, логирование происходит в указанный файл.
    Если `filename` не задан, логирование происходит в консоль.

    Args:
        filename (str, optional): Имя файла для логирования. По умолчанию None.

    Returns:
        Callable: Декоратор для логирования функции.
    """

    def decorator(func: Callable) -> Callable:
        """
        Декоратор, логирующий вызовы и результаты функции.

        Args:
            func (Callable): Функция, которую нужно логировать.

        Returns:
            Callable: Обёрнутая функция с логированием.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обёртка для логирования вызова и результата функции.

            Args:
                *args: Позиционные аргументы функции.
                **kwargs: Именованные аргументы функции.

            Returns:
                Результат выполнения обёрнутой функции.
            """
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as f:
                        print(log_message, file=f)
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        print(error_message, file=f)
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


# Пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    """
    Пример функции для демонстрации работы декоратора.

    Args:
        x (int): Первое число.
        y (int): Второе число.

    Returns:
        int: Сумма x и y.
    """
    return x + y


# Вызов функции для тестирования
my_function(1, 2)
