import calendar
from lab8.UserCalendar import UserCalendar


month = calendar.monthcalendar(2022, 3) # календарь 3го месяца (март) 2022го года
for week in month:
    week_str = ' '.join(j if j != ' 0' else '  ' for j in ['{:>2d}'.format(i) for i in week])
    print(week_str) # выводим в консоль отформатированную строку, удаляя из неё нули и выравнивая даты в колонках

print('\033[31m' + 'Привет' + '\033[32m' + ' Мир!' + '\033[0m' + ' Обычный текст') # подкрашиваем строку

cal = UserCalendar(2022, 3) # создаём пользовательский календарь и выводим на экран
print(cal)