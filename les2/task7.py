def equality(num):
    if num == 1:
        return num
    else:
        return equality(num - 1) + num


user_num = int(input('Дай число быстро: '))
if equality(user_num) == user_num * (user_num + 1) / 2:
    print('Всё верно')
