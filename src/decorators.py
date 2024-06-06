import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, 'a') as f:
                        print(log_message, file=f)
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, 'a') as f:
                        print(error_message, file=f)
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


# Пример использования
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
