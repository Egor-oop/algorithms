def even_odd(num):
    digit = num % 10
    num = int((num - num % 10) / 10)
    if num == 0:
        digits = [[], []]
        digits[digit % 2].append(digit)
        return digits
    digits = even_odd(num)
    digits[digit % 2].append(digit)
    return digits


print(even_odd(13579246803579))
