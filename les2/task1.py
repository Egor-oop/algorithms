def calculator():
    operation = str(input('Введите +, -, *, / или 0 для выхода: '))
    if operation == '0':
        return 'Пока'
    elif operation == '+':
        first_num = str(input('Введите первое число: '))
        second_num = str(input('Введите второе число: '))
        print(eval(f'{first_num} + {second_num}'))
        calculator()
    elif operation == '-':
        first_num = str(input('Введите первое число: '))
        second_num = str(input('Введите второе число: '))
        print(eval(f'{first_num} - {second_num}'))
        calculator()
    elif operation == '*':
        first_num = str(input('Введите первое число: '))
        second_num = str(input('Введите второе число: '))
        print(eval(f'{first_num} * {second_num}'))
        calculator()
    elif operation == '/':
        first_num = str(input('Введите первое число: '))
        second_num = str(input('Введите второе число: '))
        try:
            print(eval(f'{first_num} // {second_num}'))
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        calculator()


print(calculator())
