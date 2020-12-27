"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    num = 12345678908
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run('main()')

print(timeit("revers(1232347890)", setup='from __main__ import revers', number=100000))
print(timeit("revers_2(1232347890)", setup='from __main__ import revers_2', number=100000))
print(timeit("revers_3(1232347890)", setup='from __main__ import revers_3', number=100000))

"""
В cProfile мы видим, что все функции работают быстро и в оптимизации не нуждаются.
В timeit мы видим, что реализация через срез с отрицательным шагом, является самым быстрым вариантом:
1) в первом случае используется множество операций деления, поэтому самый медленный вариант решения.
2) во втором случае используется цикл + операции деления, поэтому также медленный вариант решения.
3) в третьем случае, который просто выполняет разворот посредством среза с шагом -1, 
поэтому это самый быстрый и оптимальный вариант решения.
"""
