"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random

print("Исходная функция:")


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=100))

print('Доработанная функция:')


def bubble_sort_improved(orig_list):
    n = 1
    i = 0
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                k = 1
        if i == 0:
            break
        n += 1
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=100))

"""
Время выполнения исходной функции = 5.0364009
Время выполнения доработанной функции = 5.0258978

Вывод: Время выполнения доработанной функции практически идентично со временем выполнения исходной,
поэтому в оптимизации смысла нет.
"""
