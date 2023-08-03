
# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def repeat_times(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_times(num_repeats=3)
def my_function():
    print("Hello, world!")

my_function()
