def sum_numbers():
	n = input('write the number ')
	if n == '':
		return 0
	else:
		return float(n) + sum_numbers()


print(f'sum of numbers = {sum_numbers()}')