"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
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
    return my_list


@calc_time
def dictionary_check(n):
    my_dict = dict()
    for i in range(n):
        my_dict[i] = i
    return my_dict


print("Время работы списка:")
list_check(300000)
print("Время работы словаря:")
dictionary_check(300000)