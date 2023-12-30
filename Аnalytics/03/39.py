"""
Даны два массива чисел. Требуется вывести элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел -
элементы массива. Затем записано число M – количество элементов во втором массиве. Затем элементы второго массива.

Input:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1

Output:
3 3 2 12
"""

n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

m = int(input())
list2 = list()
for i in range(m):
    x = int(input())
    list2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count += 1
    if count == 0:
        print(list1[i])
    count = 0
