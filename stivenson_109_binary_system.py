def binary(n):
	if n < 2:
		return n
	else:
		n, s = divmod(n, 2)
		return str(s) + str(binary(n))


number = int(input('write the number in decimal \nnumber system '))
print(f'your number in binary system is {binary(number)[::-1]}')