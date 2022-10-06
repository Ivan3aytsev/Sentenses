import random


def password():
	y = random.randint(7, 10)
	print('\nдлина пароля = {} символов'.format(y))
	z = ''
	for x in range(y):
		z += chr(random.randint(33, 126))
	return z


# print('случайный пароль: ', password())
