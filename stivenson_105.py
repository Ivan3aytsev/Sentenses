def int2(w, num):
	return int(w, num)


def not_ordinary(w, num):
	alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ''
	while w > 0:
		m, n = divmod(w, num)
		result += alphabet[n]
	return result[::-1]


number = input('введите число ')
num_system_in = int(input('введите число системы исчисления для входного числа {}'.format(number)))
num_system_out = int(input('введите число системы исчисления для выходного числа '))
num10 = int2(number, num_system_in)
if num_system_out == 2:
	print(f'{number} в {num_system_out}-ичной системе исчисления = {bin(num10)[2:]}')
elif num_system_out == 16:
	print(f'{number} в {num_system_out}-ичной системе исчисления = {hex(num10)[2:]}')
elif num_system_out == 8:
	print(f'{number} в {num_system_out}-ичной системе исчисления = {oct(num10)[2:]}')
else:
	print(f'{number} в {num_system_out}-ичной системе исчисления = '
				f'{not_ordinary(num10, num_system_out)}')

