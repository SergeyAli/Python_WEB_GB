"""
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K - положительное число.
Input:[1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
"""

list1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list1)

list_res = []

for i in range(k):
    list_res.append(list1[len(list1) - 1 -i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list_res)
