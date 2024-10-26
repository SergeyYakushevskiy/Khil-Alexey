numbers = [2, 21, 43, 67, 24, 67, 68, 22, 32, 27, 89, 45, 46, 20, 88]
print('Список чисел:', numbers)

numbers_sum = 0
for number in numbers:
    if number % 2 == 0:
        numbers_sum += number
print('Сумма чисел через цикл for и условный оператор:', numbers_sum)

numbers_sum = 0
index = 0
while(index < len(numbers)):
    if numbers[index] % 2 == 0:
        numbers_sum += numbers[index]
    index += 1
print('Сумма чисел через цикл while и условный оператор:', numbers_sum)

