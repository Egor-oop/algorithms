from random import randint

attempts = 10


def guessing():
    global attempts
    rnd_num = randint(0, 100)
    if attempts == 0:
        return rnd_num
    else:
        user_num = int(input('Угадайка число: '))
        if user_num == rnd_num:
            return 'Ты угадал число\nВЫ ВЫЙГРАЛИ 1.000.000$'
        else:
            attempts -= 1
            return guessing()


print(guessing())
