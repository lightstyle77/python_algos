"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


def reverse_number(my_list, rev_num=None):
    if rev_num is None:
        rev_num = []
    if len(my_list) == 0:
        new_num = ''.join(rev_num)
        print(new_num)
        return
    else:
        rev_num.append(my_list.pop())
        return reverse_number(my_list, rev_num)


@profile
def main():
    reverse_number(my_list)


my_list = (list(input('Введите число для реверса: ')))
main()

"""
Для профилирования рекурсии необходимо оборачивать её во внешнюю функцию.
Так профилировать можно, 'подводных камней' в таком профилировании не найдено.
"""
