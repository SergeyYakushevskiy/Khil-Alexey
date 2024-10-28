import locale
from datetime import datetime, timedelta

today = datetime.now().date() # текущая дата без времени
delta = timedelta(days=1) # переменная разницы дат. Хранит в себе один день
tomorrow = today + delta # дата вчеращнего дня
yesterday = today - delta # дата завтрашнего дня
print('Текущая дата:', today)
print('Завтра:', today + delta)
print('Вчера:', today - delta)
print('Сегодня - вчера =', today - yesterday) # 1 = день уже прошёл
print('Сегодня - завтра =', today - tomorrow) # -1 = день ещё не наступил
print('Сегодня == завтра: ', today == tomorrow)
print('Сегодня == вчера: ', today == yesterday)
print('Вчера == завтра: ', yesterday == tomorrow)
some_date = datetime(year=2022, month=12, day=20, hour=15, minute=20) # задаём дату
print('Некоторая дата: ', some_date)
delta = timedelta(days=2 * 30 + 5, hours=3) # задаём разницу в 2 месяца по 30 дней + 5 дней и 3 часа
print('delta =', delta)
print(some_date, '+', delta, '=', some_date + delta)
new_date = datetime(year=2018, month=4, day=12, hour=11, minute=23) # задаём новую дату
locale.setlocale(locale.LC_TIME, 'ru') # задаём местность, чтобы поменять язык на русский
print(new_date.strftime("%d %h %Y %H:%M")) # выводим новую дату в формате день месяц год час:минута
