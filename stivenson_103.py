from Stivenson_100 import password
from Stivenson_102 import checkPassword
count = 0
while True:
	a = password()
	print('случайный пароль: ', a)
	print(checkPassword(a))
	count += 1
	print('попытка №', count)
	if checkPassword(a):
		break

