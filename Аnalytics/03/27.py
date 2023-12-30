"""
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.,

Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

Output: 14
"""

stroka = input().split()

set_1 = set()
for i in stroka:
    set_1.add(i.lower())

print(len(set_1))
