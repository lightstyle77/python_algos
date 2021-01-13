"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile


# задача: определение минимального числа в массиве.
# через цикл
@profile
def func_min_val():
    my_list = list(range(100000))
    min_val = my_list[0]
    for el in my_list[1:len(my_list)]:
        if el < min_val:
            min_val = el
    return min_val


# через встроенную функцию
@profile
def func_min_2():
    my_list = list(range(100000))
    return min(my_list)


if __name__ == "__main__":
    func_min_val()
    func_min_2()

"""
Для запуска программы, через цикл выделяется - 19,4 Mib, через встроенную функцию - 19.7 MiB.
Через цикл, памяти используется больше на 0,8 Mib - на 33 строке для проведения 
операция цикла было выделено больше памяти.
Вариант через встроенную функцию - наиболее эффективно использует память.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     19.4 MiB     19.4 MiB           1   @profile
    30                                         def func_min_val():
    31     23.2 MiB      3.8 MiB           1       my_list = list(range(100000))
    32     23.2 MiB      0.0 MiB           1       min_val = my_list[0]
    33     24.0 MiB      0.8 MiB      100000       for el in my_list[1:len(my_list)]:
    34     24.0 MiB      0.0 MiB       99999           if el < min_val:
    35                                                     min_val = el
    36     24.0 MiB      0.0 MiB           1       return min_val



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.7 MiB     19.7 MiB           1   @profile
    41                                         def func_min_2():
    42     23.2 MiB      3.5 MiB           1       my_list = list(range(100000))
    43     23.2 MiB      0.0 MiB           1       return min(my_list)
    
Python 3.9.1
Windows 10 64-bit    
    
"""