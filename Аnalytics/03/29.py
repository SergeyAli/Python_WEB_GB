"""
Петя и Вася поспорил кто быстрее решит следующую задачу: "Задана последовательность неотрицательных целых чисел.
Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившемся нулем
(число 0 не входит в последовательность)". Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог
до конца сделать задание. Они решили так: у кого будет меньше ошибок к коде, тот и выиграл спор.
За помощью товарищи обратились к Вас, студентам.

Input:

Output:
"""

n = int(input())
max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
