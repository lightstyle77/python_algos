"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
import timeit

my_list = [uniform(0, 50) for _ in range(5)]


def merge(left_list, right_list):
    result = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    result += left_list[i:] + right_list[j:]
    return result


def merge_sort(left_list):
    if len(left_list) <= 1:
        return left_list
    else:
        left = left_list[:len(left_list) // 2]
        right = left_list[len(left_list) // 2:]
    return merge(merge_sort(left), merge_sort(right))


print(f'Не отсортированный список: {my_list}')
print(f'Отсортированный список: {merge_sort(my_list)}')

print(f'Время выполнения сортировки методом слияния - '
      f'{timeit.timeit("merge_sort(my_list)", setup="from __main__ import merge_sort, merge, my_list", number=10000)}')

'''
Не отсортированный список: [22.53852153164997, 33.51811276208841, 24.427235162702527, 39.27216098068127, 
24.941485708015854]
Отсортированный список: [22.53852153164997, 24.427235162702527, 24.941485708015854, 33.51811276208841, 
39.27216098068127]
Время выполнения сортировки методом слияния - 0.07583580000000001
'''