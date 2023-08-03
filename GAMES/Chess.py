# 3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from Func_Pac.queens import generation_successful
# import itertools
# import random
#
# def queens(queens_positions):
#
#     for i in range(len(queens_positions)):
#
#         for j in range(i+1, len(queens_positions)):
#             row1, col1 = queens_positions[i]
#             row2, col2 = queens_positions[j]
#
#         if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1-col2):
#             return False
#     return True
#
#
# def generation_successful():
#     successful_args = []
#
#     permutations = list(itertools.permutations(range(1,9)))
#     random.shuffle(permutations)
#
#     for permutation in permutations:
#         queens_positions = [(i+1, permutation[i]) for i in range(8)]
#         if queens(queens_positions):
#             successful_args.append(queens_positions)
#             if len(successful_args) ==4:
#                 break
#
#     return successful_args
#
successful_arrangements = generation_successful()
print("4 успешных расстановки")
for i, arrangement in enumerate(successful_arrangements, 1):
    print(f'Расстановка {i}: {arrangement}')

