def factor(n):
	if n == 1:
		return n
	else:
		return n * factor(n - 1)


num = int(input('num = '))
print(factor(num))