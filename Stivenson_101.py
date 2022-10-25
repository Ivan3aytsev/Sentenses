import random


def car_number():
	y = random.choice(['old', 'new'])
	three_symbols = ''.join([chr(random.randint(97, 122)) for _ in range(3)])
	three_numbers = ''.join([chr(random.randint(48, 57)) for _ in range(3)])
	four_numbers = ''.join([chr(random.randint(48, 57)) for _ in range(4)])
	if y == 'old':
		number = three_symbols + three_numbers
	else:
		number = four_numbers + three_symbols
	print('номер машины: {}'.format(number))


car_number()