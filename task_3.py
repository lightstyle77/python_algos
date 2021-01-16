"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from statistics import median
import random
import timeit


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


m = int(input("Введите натуральное число m: "))
orig_list = [random.randint(-10, 10) for i in range((2 * m) + 1)]
print(f'Исходный массив: {orig_list}')
print(f'Отсортированный массив: {shell(orig_list)}')


def shell_med(sort_list):
    return shell(sort_list)[len(sort_list) // 2]


print(f'Медиана отсортированного массива: {shell_med(orig_list)}')
print(timeit.timeit("shell_med(orig_list[:])", setup="from __main__ import orig_list, shell_med", number=10000))

print(f'Медиана через встроенную ф-цию: {median(orig_list)}')
print(timeit.timeit("median(orig_list[:])", setup="from __main__ import orig_list, median", number=10000))

"""
Введите натуральное число m: 5
Исходный массив: [-9, -8, -10, -10, 9, -4, 5, -10, 9, 1, -9]
Отсортированный массив: [-10, -10, -10, -9, -9, -8, -4, 1, 5, 9, 9]
Медиана отсортированного массива: -8
0.06296629999999981
Медиана через встроенную ф-цию: -8
0.0064006000000000896

Вывод: Медиана через встроенную функцию работает значительно быстрее, чем поиск через сортировку массива.
"""
