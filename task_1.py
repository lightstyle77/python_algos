"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: Если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def calc_time(func):
    def my_func(*args):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)

    return my_func


@calc_time
def list_check(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
        my_list.index(i)
    return my_list


@calc_time
def dictionary_check(n):
    my_dict = dict()
    for i in range(n):
        my_dict[i] = i
        my_dict.get(i)
    return my_dict


print("Время работы списка:")
list_check(30000)
print("Время работы словаря:")
dictionary_check(30000)

# На данном примере видно, что словарь работает значительно быстрее, чем список.
