import sqlite3 as sql # библиотека для работы с базами данных типа sqlite

def connect_to_db(db_path): # функция для подключения к бд
    connection = sql.connect(db_path)
    cursor = connection.cursor()
    return [connection, cursor]

def print_table(table_list, column_length = 10, cell_separator=''): # функция красивого вывода содержимого
                                                                    # таблицы на экран
                                                                    # сolumn_length - ширина ячейки
                                                                    # cell_separator - разделитель между ячейками
    cell = '{:<' + str(column_length) + '}' # Ячейка будет строкой, в которой значение выравнивается по левому краю
    for row in table_list: # форматируем значения таблицы под формат ячейки и выводим построчно на экран,
        print(cell_separator.join([cell.format(elem) for elem in row]))



def execute_select(cursor, select_query): # функция выборки данных из бд.
                                          # курсор взаимодействует с базой данных, выполняя некоторый запрос select_query
                                          # результат выполнения запроса передаётся дальше в программу
    cursor.execute(select_query)
    result = cursor.fetchall()
    return result


connection, cursor = connect_to_db('ToolMachines.db') # создаём подключение
print(f'Подключение к {'ToolMachines.db'} успешно')

select_dicShops = execute_select(cursor, 'select * from dicShops') # выбираем все данные из таблицы dicShops
dicShops = [['№ цеха', 'Название цеха']] # Первой строкой таблицы будут заголовки столбцов
dicShops.extend(select_dicShops) # добавляем результат выборки данных из БД
print_table(dicShops) # красиво выводим на экран

number = 0 # переменная хранит в себе номер цеха, который введёт пользователь
workshop_numbers = [row[0] for row in dicShops[1:]] # задаём все допустимые значения номеров цехов
while number not in workshop_numbers:
    try:
        number = int(input('Введите номер цеха: ')) # пробуем перевести то, что ввёл пользователь, в число
                                                    # на этом месте может возникнуть ошибка Exception
                                                    # это значит, что пользователь ввёл неверные данные
        if number not in workshop_numbers: # если же пользователь ввёл число, но оно не входит в диапазон номеров
                                           # цехов, то вручную вызываем ошибку чтобы в дальнейшем её обработать
            raise Exception()
    except Exception: # обрабаываем ошибку, если она возникнет
        print(f'№ цеха = {number} нет в списке.', end='')
        resume = input('Продолжить? [Да/Нет]: ')
        while resume != 'Да' and resume != 'Нет': # пока пользователь не введёт "Да" или "Нет",
                                                  # программа дальше не будет работать
            resume = input('Продолжить? [Да/Нет]: ')
        if resume == 'Нет':
            exit(0)

select_machines = execute_select(cursor, f"""SELECT
 dicGroupToolMachines.Name,
 dicModelToolMachine.Name,
 dicInvNumToolMachines.InvNumber
FROM
 dicShops INNER JOIN dicToolMachinesShops
 ON dicShops.Id = dicToolMachinesShops.IdShop
 INNER JOIN dicInvNumToolMachines
 ON dicToolMachinesShops.InvNumber =
dicInvNumToolMachines.InvNumber
 INNER JOIN dicGroupToolMachines
 ON dicInvNumToolMachines.IdGroup = dicGroupToolMachines.Id
 INNER JOIN dicModelToolMachine
 ON dicInvNumToolMachines.IdModel = dicModelToolMachine.Id
WHERE
 dicShops.Id ={int(number)}""") #Выполняем запрос из условия задания, вставляя полученный номер цеха

machines = [['Группа', 'Модель', 'Инв. №']] # первая строка таблицы - заголовки
machines.extend(select_machines) # Добавляем результат выборки данных
print_table(machines, column_length=18, cell_separator=' | ') # Красиво выводим таблицу, увеличивая ширину ячейки и
                                                              # добавляя разделитель между ними
