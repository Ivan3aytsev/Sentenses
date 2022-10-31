def higer_year(y):
	if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
		return True
	# високосный год
	else:
		return False


def count_days(y, m):
	a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if higer_year(y):
		return b[m - 1]
	else:
		return a[m - 1]


# year = int(input('write year '))
# month = int(input('write month '))
# print(count_days(year, month))
