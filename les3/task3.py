import hashlib

user_str = input('Введите строку на английском: ')
a = set()

N = len(a)
for i in range(N):
    if i == 0:
        N = len(user_str) - 1
    else:
        N = len(user_str)
    for j in range(N, i, -1):
        a.add(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())


print(f'Кол-во подстрок "{user_str}" - {len(a)}')
