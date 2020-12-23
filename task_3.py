"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

word = "papa"
hash_set = set()
substrings = set()
for i in range(len(word)):
    for j in range(len(word), i, -1):
        temp_string = word[i:j]
        if temp_string != word:
            substrings.add(temp_string)
            hash_set.add(hashlib.sha256(temp_string.encode()).hexdigest())
print(hash_set)
print(substrings)
print(f'В строке "{word}" {len(hash_set)} различных подстрок')
