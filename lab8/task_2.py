import calendar

cal = calendar.LocaleTextCalendar(locale='ru_RU', firstweekday=0)
print(cal.formatyear(2023)) # выводим календарь 2023 года, основываясь на местности, меняем язык на русский и начало недели с понедельника