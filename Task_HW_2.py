# 2. Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import csv
from random import randint as r
from typing import Callable
import json
from pathlib import Path
from functools import wraps


def deco_read(func1: Callable) -> None:
    @wraps(func1)
    def wrapper_a(*args):
        with open("number_list.csv", 'r', newline='') as f:
            csv_file = csv.reader(f)
            for i, line in enumerate(csv_file):
                if i == 0:
                    continue
                else:
                    row = ''.join(line)
                    params = row.split()
                    params = [int(j) for j in params]
                    result = func1(params)
        return result

    return wrapper_a


def deco_json(func: Callable):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args):
        result = func(*args)
        d = {f"{args}": result, }
        data.append(d)

        with open(file, 'w', encoding='utf-8') as f2:
            json.dump(data, f2, ensure_ascii=False, indent=2)

        return result

    return wrapper


@deco_read
@deco_json
def quadratic_equation(list_of_num: list):
    a = list_of_num[0]
    b = list_of_num[1]
    c = list_of_num[2]
    D = b ** 2 - 4 * a * c

    if D < 0:
        return 'NO result'
    elif D == 0:
        return (-b / (2 * a))
    else:
        x1 = (-b + (D) ** 0.5) / (2 * a)
        x2 = (-b - (D) ** 0.5) / (2 * a)
        return (x1, x2)


def write_csv(file_name: str) -> None:
    rows = r(100, 1001)
    count = 3

    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for i in range(rows):
            lines = []
            for _ in range(count):
                a = r(1, 100)
                lines.append(a)
            if i == 0:
                csv_write.writerow(['num_1', 'num_2', 'num_3'])
            else:
                csv_write.writerow(lines)


if __name__ == '__main__':
    write_csv("number_list.csv")
    quadratic_equation()






