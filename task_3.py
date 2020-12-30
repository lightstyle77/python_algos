"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from random import randint
from timeit import timeit

lst_obj = []
deq_obj = deque()
ARRAY_SIZE = 50


def lst_app_start(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.insert(0, randint(0, 1000))


def deq_app_start(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.appendleft(randint(0, 1000))


def lst_ins(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.insert(2 * randint(0, 1000), randint(0, 1000))


def deq_ins(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.insert(2 * randint(0, 1000), randint(0, 1000))


def lst_pop_end(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.pop()


def deq_pop_end(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.pop()


def lst_pop_start(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.pop(0)


def deq_pop_start(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.popleft()


print("\n1) Проверка добавления элементов в начало массива.\n")
print("list: ", timeit("lst_app_start(lst_obj)", setup="from __main__ import lst_app_start, lst_obj", number=1000))
print("deque: ", timeit("deq_app_start(deq_obj)", setup="from __main__ import deq_app_start, deq_obj", number=1000))

print("\n2) Проверка добавления элементов в тело массива.\n")
print("list: ", timeit("lst_ins(lst_obj)", setup="from __main__ import lst_ins, lst_obj", number=1000))
print("deque: ", timeit("deq_ins(deq_obj)", setup="from __main__ import deq_ins, deq_obj", number=1000))

print("\n3) Проверка извлечения элементов с конца массива.\n")
print("list: ", timeit("lst_pop_end(lst_obj)", setup="from __main__ import lst_pop_end, lst_obj", number=1000))
print("deque: ", timeit("deq_pop_end(deq_obj)", setup="from __main__ import deq_pop_end, deq_obj", number=1000))

print("\n4) Проверка извлечения элементов с начала массива.\n")
print("list: ", timeit("lst_pop_start(lst_obj)", setup="from __main__ import lst_pop_start, lst_obj", number=1000))
print("deque: ", timeit("deq_pop_start(deq_obj)", setup="from __main__ import deq_pop_start, deq_obj", number=1000))


"""
В извлечении элементов с конца массива - list и deque примерно одинаковы по скорости. 
А вот в добавлении элементов в начало и тело массива и 
извлечении элементов с начала массива - deque значительно быстрее, чем list.
"""