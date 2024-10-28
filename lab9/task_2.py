import xml.etree.ElementTree as etree

def print_student(student_dict): # Красивый вывод студента
    print(student_dict.get('Фамилия')) # Вывод имени студента
    print('-' * 32) # Разделительная строка
    disciplines = list(student_dict.keys()) # задание списка предметов, которые закрыл студент
    if 'Фамилия' in disciplines:
        disciplines.remove('Фамилия') # в списке сохраняется ключ "Фамилия", поэтому его надо удалить
    for desc in disciplines:
        print('{:>30}{:>2}'.format(desc, student_dict.get(desc))) # формат вывода данных о
                                                                        # предмете с выравниванием по правому краю

tree = etree.parse('task_xml.xml') # выполняем считываение xml-файла
root = tree.getroot() # получаем корневой тег. В данном случае, group

for student in root.findall('student'): # в теге group хранятся блоки student. Обрабатываем каждый
    row = {'Фамилия': student.attrib.get('name')} # создаём словарь на основе данных о студенте
    for desc in student:
        row[desc.tag] = desc.text
    print_student(row) # вывод данных о студенте в консоль в удобочитаемом формате
