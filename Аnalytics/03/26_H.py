"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число A в целую степень B с помощью рекурсии

Input:
A = 3; B = 5
A = 2; B = 3

Output:
-> 243
-> 8
"""

def recApowB(a, b):
    if b == 0:
        return 1
    return a * recApowB(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(recApowB(a, b))
