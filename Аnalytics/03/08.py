"""
Требуеться опредилить, можно ли от шоколадки размером n x m долек отломить k долек, если разрешаеться сделать один
разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)
324 -> yes
321 -> no
"""

n = 3
m = 2
k = 1

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')