def revers_num(num):
    num2 = 0
    if num > 0:
        return num2
    else:
        num2 *= 10
        num2 += num % 10
        num /= 10
        return revers_num(num)  # num или num2 то возращает 0


print(revers_num(2346462))
