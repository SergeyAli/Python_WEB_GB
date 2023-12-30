"""
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.

Input:
print_operation_table(lambda x, y: x * y,6,6)
Output:
 1 2 3 4 5 6
 2 4 6 8 10 12
 3 6 9 12 15 18
 4 8 12 16 20 24
 5 10 15 20 25 30
 6 12 18 24 30 36
"""

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>1}" for x in i])
#
#
# print_operation_table(lambda x, y: x * y,6,6)
# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows <= 2 or num_columns <=2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         # a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#         # for i in a:
#         #     print(*[f"{x:>1}" for x in i])
#         a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#         for i in a:
#             print(*[f"{x:}" for x in i])

# num_columns = 6
#
# for i in range(1, num_columns + 1):
#     print(*[f"{i:}"], end=' ')

def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows <= 2 or num_columns <=2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in range(1, num_columns + 1):
            print(*[f"{i:}"], end=' ')
        print(end='\n')
        a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        for i in a:
            print(*[f"{x:}" for x in i])

# print_operation_table(lambda x, y: x * y, 3, 3)
# Ожидаемый ответ:
# 1 2 3
# 2 4 6
# 3 6 9
#
# print_operation_table(lambda x, y: x + y, 4, 4)
# Ожидаемый ответ:
# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8
#
print_operation_table(lambda x, y: x - y, 5, 5)
# Ожидаемый ответ:
# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0
#
# print_operation_table(lambda x, y: x * y, 1, 2)
# Ожидаемый ответ:
# ОШИБКА! Размерности таблицы должны быть больше 2!
#
# print_operation_table(lambda x, y: x / y, 4, 4)
# Ожидаемый ответ:
# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0
#
# print_operation_table(lambda x, y: x * y)
# Ожидаемый ответ:
#  1 2 3 4 5 6 7 8 9
#  2 4 6 8 10 12 14 16 18
#  3 6 9 12 15 18 21 24 27
#  4 8 12 16 20 24 28 32 36
#  5 10 15 20 25 30 35 40 45
#  6 12 18 24 30 36 42 48 56
#  7 14 21 28 35 42 49 46 63
#  8 16 24 32 40 48 56 64 72
#  9 18 27 36 45 54 63 72 81

# n = int(input())
# n1 = int(input())
# sep = ' '
# for i in range(1, n+1):
#     for j in range(1, n1+1):
#         z = i / j
#         print(z, end = sep)
#     print()