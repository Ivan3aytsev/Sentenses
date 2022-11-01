def nod(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
	else:
		return nod(b % a, a)


first = int(input('write the first number '))
second = int(input('write the second number '))
print(f'NOD = {nod(first, second)}')