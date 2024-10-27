import cmath
import math

def solve_simple_operation(numbers, operation):
    numbers = [int(i) for i in numbers] # Переводим каждое число в списке из строкового типа в численный
    result = ''
    if operation == '+':
        result =  sum(numbers)
    elif operation == '-':
        result = numbers[0] - numbers[1]
    elif operation == '*':
        result = numbers[0] * numbers[1]
    elif operation == '/':
        if (numbers[1] != 0):
            result = numbers[0] / numbers[1]
        else:
            result = 'Ошибка'
            print('Нельзя делить на 0')
    else:
        print('Неизвестная операция')
    print(numbers[0], operation, numbers[1], '=', result)
    return result


def get_average(numbers):
    if(len(numbers)) == 0:
        print('Список пуст')
        return
    numbers = [int(i) for i in numbers]
    average = sum(numbers) / len(numbers)
    print('СРД(',*numbers,')=',average)
    return average

def get_sum(numbers):
    numbers = [int(i) for i in numbers]
    sum_num = sum(numbers)
    print('СУМ(',*numbers,')=',sum_num)
    return sum_num

def solve_square(a, b, c):
    if a == 0:
        if b != 0:
            return [-c / b]
        return [-c]
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x_1 = (-b + math.sqrt(disc) )/ 2 * a
        x_2 = (-b - math.sqrt(disc) )/ 2 * a
        return [x_1, x_2]
    elif disc == 0:
        x = -b / 2 * a
        return [x, x]
    else:
        x_1 = (-b + cmath.sqrt(disc))/ 2 * a
        x_2 = (-b - cmath.sqrt(disc))/ 2 * a
        return [x_1, x_2]


instruction = """
Обычный калькулятор: КАЛК или CALC
Сумма значений: СУМ или SUM
Среднее арифметическое: СРД или AVR
Квадратное уравнение: КВУР bkb SQ
Выйти из режима: введите любой другой символ    
"""

while(True):
    print('Новое вычисление:')
    print(instruction)
    comand = input('Введите команду: ')
    match comand.upper():
        case 'КАЛК' | 'CALC':
            query = input('Введите 2 числа и операцию через пробел: ').split(' ')
            solve_simple_operation(query[0:2], query[2])
        case 'СУМ' | 'SUM':
            query = input('Введите последовательность чисел через пробел:').split(' ')
            get_sum(query)
        case 'СРД' | 'AVR':
            query = input('Введите последовательность чисел через пробел:').split(' ')
            get_average(query)
        case 'КВУР' | 'SQ':
            print('РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ')
            print('Ax² + Bx + C = 0')
            print('Введите коэффициенты уравнения:\n')
            a = int(input('A = '))
            b = int(input('B = '))
            c = int(input('C = '))
            result = solve_square(a, b, c)
            print('Корни:')
            for root in result:
                print(root)
        case _:
            exit(0)
