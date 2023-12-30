"""
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой
характеристики, и возвращает True, если это так. Если значение характеристики для разных объектов отличается – то False.
Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic – это функция, которая принимает
объект и вычисляет его характеристику.

Input:
values = [0,2,10,6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
Output:
same
"""

def same_by(characteristic, object):
    result = True
    list1 = [characteristic(x) for x in object]
    for i in range(len(list1) - 1):
        if list1[i] != list1[i+1]:
            result = False
    return result

values = [0,2,10,6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')