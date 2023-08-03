from random import randint

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
