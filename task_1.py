"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1([0, 1, 2, 3, 4, 5, 6, 7])", setup="from __main__ import func_1"))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(timeit("func_2([0, 1, 2, 3, 4, 5, 6, 7])", setup="from __main__ import func_2"))


def func_3(nums):
    new_arr = nums[::2]
    return new_arr


print(timeit("func_3([0, 1, 2, 3, 4, 5, 6, 7])", setup="from __main__ import func_3"))

"""
1. Добавлено два решения - func_2 и funс_3.
2. Решение func_2 реализовано через генераторное выражение, которое работает немного быстрее.
3. Решение func_3 реализовано через срез с шагом 2, скорость значительно выросла, так как удалось избавится от цикла и
операции деления, которые замедляют процесс.
"""