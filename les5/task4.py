from timeit import timeit
import collections


def normal_dict():
    dict_test = {'a': 1, 'b': 2, 'c': 3}
    dict_test['d'] = 4
    del dict_test['a']


def order_dict_dict():
    dict_test = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    dict_test.update(('d', 4))
    del dict_test['d']


print('################ normal_dict ################')
print(
    timeit(
        'normal_dict',
        setup='from __main__ import normal_dict',
        number=10000))

print('################ order_dict_dict ################')
print(
    timeit(
        'order_dict_dict',
        setup='from __main__ import order_dict_dict',
        number=10000))


"""Вывод:
################ normal_dict ################
0.0001436999999999966
################ order_dict_dict ################
0.00014360000000000067

В python > 3.6 OrderedDict нужен потамучто в этих версиях словарь не сохраняет свои позиции
"""
