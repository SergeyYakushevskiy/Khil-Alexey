# def name(parameter1, parameter2, ...)
#   создание функции под названием main, которая на основе параметров
#   parameter1 и parameter2 вычисляет значение и выдаёт его оператором return
#   функция суммы чисел
def sum_operands(operand1, operand2):
    return operand1 + operand2

# функция вычитания одного числа из другого
def sub_opearnds(operand1, operand2):
    return operand1 - operand2

# функция умножения чисел
def mult_operand(operand1, operand2):
    return operand1 * operand2

# функция деления чисел
def div_operands(operand1, operand2):
    return operand1 / operand2

# функция возведения в степень числа
def construct_operands(foundation, degree):
    return foundation ** degree

# функция нахождения целой части от деления числа operand1 на operand2
def int_div_operands(operand1, operand2):
    return operand1 // operand2

# задаём операнды
operand_1 = 45
operand_2 = 12
operand_3 = 23.12
operand_4 = 3.22
operand_5 = 3 + 4j
operand_6 = 5 + 10j

#Вывод операндов на экран:
print('Операнд 1:', operand_1)
print('Операнд 2:', operand_2)
print('Операнд 3:', operand_3)
print('Операнд 4:', operand_4)
print('Операнд 5:', operand_5)
print('Операнд 6:', operand_6)
print() # пустая строка
# выводим на экран результаты функций
print(operand_1, '+', operand_2, '=', sum_operands(operand_1, operand_2))
print(operand_3, '+', operand_4, '=', sum_operands(operand_3, operand_4))
print(operand_5, '+', operand_6, '=', sum_operands(operand_5, operand_6))
print() # пустая строка
print(operand_1, '-', operand_2, '=', sub_opearnds(operand_1, operand_2))
print(operand_3, '-', operand_4, '=', sub_opearnds(operand_3, operand_4))
print(operand_5, '-', operand_6, '=', sub_opearnds(operand_5, operand_6))
print() # пустая строка
print(operand_1, '*', operand_2, '=', mult_operand(operand_1, operand_2))
print(operand_3, '*', operand_4, '=', mult_operand(operand_3, operand_4))
print(operand_5, '*', operand_6, '=', mult_operand(operand_5, operand_6))
print() # пустая строка
print(operand_1, '/', operand_2, '=', div_operands(operand_1, operand_2))
print(operand_3, '/', operand_4, '=', div_operands(operand_3, operand_4))
print(operand_5, '/', operand_6, '=', div_operands(operand_5, operand_6))
print() # пустая строка
print(operand_1, '**', operand_2, '=', construct_operands(operand_1, operand_2))
print(operand_3, '**', operand_4, '=', construct_operands(operand_3, operand_4))
print(operand_5, '**', operand_6, '=', construct_operands(operand_5, operand_6))
print() # пустая строка
print(operand_1, '//', operand_2, '=', int_div_operands(operand_1, operand_2))
print(operand_3, '//', operand_4, '=', int_div_operands(operand_3, operand_4))
print(operand_5, '//', operand_6, '=', int_div_operands(operand_5, operand_6))
# Возникает ошибка при целочисленном делении комплексных чисел,
# так как нет целого числа от результата такой операции
