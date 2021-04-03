from collections import deque
from timeit import timeit


def deque_list():
    lst = list('hello')
    deq_obj = deque(lst)
    deq_obj.append('e')
    deq_obj.appendleft('a')
    deq_obj.pop()
    deq_obj.popleft()
    return deq_obj


def normal_list():
    lst = list('hello')
    lst.append('e')
    # lst.appendleft('a') - метода appendleft НЕТ у обычных списков
    lst.pop()
    # lst.popleft() - метода popleft НЕТ у обычных списков
    return lst


print('################ deque ################')
print(
    timeit(
        'deque_list',
        setup='from __main__ import deque_list',
        number=10000))

print('################ list ################')
print(
    timeit(
        'normal_list',
        setup='from __main__ import normal_list',
        number=10000))


"""Вывод:
################ deque ################
0.00017110000000000042
################ list ################
0.00017059999999999992
Сдесь список тратит на 1 миллионную меньше потаму-что в варианте с деком используется больше методов"""
