# Магическими называются даты, в которых произведение дня и месяца
# составляет последние две цифры года. Например, 10 июня 1960 года –
# магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
# ющую, является ли введенная дата магической. Используйте написан-
# ную функцию в главной программе для отображения всех магических
# дат в XX веке.
# Возможно, вам пригодится здесь функция, разработанная
# в упражнении 106.

from stivenson_106 import *
def magic_date(d, m, y):
	if d * m == y % 100:
		return True
	else:
		return False


# day = int(input('write the day '))
# month = int(input('write the month '))
# year = int(input('write the year '))
count = 0
for years in range(1900, 2025):
	for months in range(1, 13):
		for days in range(1, count_days(years, months)):
			if magic_date(days, months, years):
				count += 1
				print(f'the date {days}.{months}.{years} is MAGIC DATE')
print(f'Total amount MAGIC days is {count}')


# if magic_date(day, month, year):
# 	print(f'the date {day}.{month}.{year} is MAGIC DATE')
# else:
# 	print(f'the date {day}.{month}.{year} is ordinary DATE')


