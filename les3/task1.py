"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import time


def how_many_time(func):
    start_val = time.time()
    res = 0

    for i in range(1, 10000 + 1):
        res += i

    end_val = time.time()

    print(res, end_val - start_val)


my_dict = {}
my_list = []


@how_many_time
def module_a(list_arg, dict_arg):
    for i in list_arg:
        my_list.append(i)

    keys = range(len(dict_arg))
    for j in keys:
        my_dict[j] = dict_arg[j]

    return my_dict, my_list


print(module_a(['hello', 'hahaha'], ['first', 'last']))
