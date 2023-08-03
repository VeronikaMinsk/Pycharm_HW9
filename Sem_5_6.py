# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# Задание №6
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


from typing import Callable
import json
import os
from random import randint
from functools import wraps


def fun_decor_file(fun: Callable) -> Callable[..., None]:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        spam_dict = dict()

        file_json = f'{fun.__name__}.json'
        if os.path.exists(file_json):
            with open(file_json, 'r', encoding='utf-8') as fj:
                spam_dict = json.load(fj)

        spam_dict[str(args)] = args
        spam_dict.update(**kwargs)
        spam_dict['result'] = fun(*args, **kwargs)

        with open(file_json, 'w', encoding='utf-8') as fj:
            json.dump(spam_dict, fj, indent=2, ensure_ascii=False)

    return wrapper


def fun_decor_control_values(fun: Callable) -> Callable[..., None]:
    @wraps(fun)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg not in range(1, 101):
                raise ValueError(f"Аргументы должны быть целыми числами в диапазоне от 1 до 100: {args}")
        for key, value in kwargs.items():
            if not isinstance(value, int) or value not in range(1, 11):
                raise ValueError(f"Значения именованных аргументов должны быть целыми числами в диапазоне от 1 до 10: {kwargs}")
        return fun(*args, **kwargs)

    return wrapper


def fun_decor_repeat(num_repeats: int) -> Callable:
    def decorator(fun: Callable) -> Callable:
        @wraps(fun)
        def wrapper(*args, **kwargs):
            for _ in range(num_repeats):
                result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator


@fun_decor_file
@fun_decor_control_values
@fun_decor_repeat(num_repeats=3)
def fun_secret(num: int, count: int):
    current_num = randint(1, num)
    for item in range(1, count + 1):
        spam = int(input(f'введите число в диапазоне от 1 до {num} (попытка № {item} из {count}): \n'))
        if spam == current_num:
            print('верно')
            break
        elif spam > current_num:
            print('меньше')
        else:
            print('больше')


if __name__ == '__main__':
    fun_secret(50, 8)
