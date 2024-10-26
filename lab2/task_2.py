is_continue = True # выключает цикл, когда пользователь не хочет больше ничего вычислять
while is_continue:
    params = input('Введите 2 числа и операцию через пробел: ').split(' ') # Например: 2 3 +
    a = float(params[0]) #программа работает с вещественными числами, записанными через точку
    b = float(params[1])
    operation = params[2]
    print('Новое вычисление:\n')
    print('a =',a)
    print('Операция:', operation)
    print('b =',b)
    result = 0
    # определение оперции, которую пользователь хочет выполнить
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if(b != 0):
            result = a / b
            print('Результат:', a, operation, b, '=', result)
        else:
            result = 'Ошибка'
            print('Нельзя делить на 0')
    else:
        print('Неизвестная операция') # выводится, когда пользователь указал операцию неверно
    print('Результат:', a, operation, b, '=', result)
    answer = input('Продолжить? ').lower() # Пользователь должен ввести либо д, либо н.
                                           # Неважно. большую или маленькую
    while(answer != 'д' and answer != 'н'):
        answer = input('Продолжить? ').lower()
    is_continue = True if answer == 'д' else False