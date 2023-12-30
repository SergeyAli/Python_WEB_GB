"""
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовём самой далёкой планетой ту, орбита которой имеет самую
большую площадь.Напишите функцию findFarthestOrbit(list_of_orbits), которая среди списка орбит планет найдет ту, по
которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины
полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел – полуосей её
эллипса. Площадь эллипса вычисляется по формулеS = Pi * a * b, где a и b– длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую
площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далёкая планета ровно одна

Input:
orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
print(*find_farthest_orbit(orbits))
Output:
2.5 10
"""
from math import pi

def find_farthest_orbit(list_of_orbits):
    list1 = [i for i in list_of_orbits if i[0] != i[1]]
    list_s = [(pi * i[0] * i[1]) for i in list1]
    max_s = list_s.index(max(list_s))

    return list1[max_s]


orbits = [(1,3), (2.5,10), (7,2), (6,6), (4,3)]
print(*find_farthest_orbit(orbits))
# find_farthest_orbit(orbits)
