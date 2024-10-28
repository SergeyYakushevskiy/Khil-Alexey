def get_formatted_data(file_path):
    """Открываем файл только для чтения с кодировкой utf-8"""
    with open(file_path, 'r', encoding='UTF-8') as data:
        rows = [] # в первой строке будут заголовки колонок
        column_headers = ['Фамилия'] # уникальные заголовки колонок, которые будут добавляться по мере чтения файла
        for row in data.readlines():
            split_row = row.split(';') # раздлеяет строку на фамилию и предметы. Фамилию записываем в словарь под ключом "Фамилияц"
            student = {'Фамилия' : split_row[0]}
            for desc in split_row[1:]:
                desc_row = desc.split(':') # получает оценку по конкретному прдемету и записывает в словарь в формате Предмет:оценка
                if desc_row[0] not in column_headers:
                    column_headers.append(desc_row[0])
                student[desc_row[0]] = desc_row[1].replace('\n', '')
            rows.append(student)
    return [column_headers, rows] # на выходе из функции получается список заголовков и строк данных, где строка - это словарь колонка:значение


def write_data_into_file(file_path, data):
    column_length = 15 # для выравнивания колонок задаётся ширина колонки
    with open(file_path, 'w+', encoding='UTF-8') as file:
        header = ''
        for column_header in data[0]: # запись заголовков в колонки строки
            header += ('{:^' + str(column_length) + '}').format(column_header) + '|'
        line_border = '-' * len(header) # вычисление ширины таблицы, создание подчёркивающей линии
        file.write(header + '\n' + line_border) # запись заголовков в файл
        print(header + '\n' + line_border)
        for row in data[1]: # итерация по строкам данных
            row_str = ''
            for key in data[0]: # итерация по уникальным колонка. Если в конкретной строке есть информация по данной
                                # колонке, то записываем, если нет, то ставим прочерк "-". В конце для удобства
                                # чтения добавляем разделитель ячеек "|"
                row_str += ('{:^' + str(column_length) + '}').format(row.get(key) if key in row.keys() else'-') + '|'
            file.write('\n' + row_str + '\n' + line_border) # запись отформатированной строки в файл
            print(row_str + '\n' + line_border)

data = get_formatted_data('data.txt') # считываем данные, основываясь на заданном пути к файлу, и сразу форматируем
write_data_into_file('out.txt', data) #записываем отформатированные данные в новый файл out.txt
