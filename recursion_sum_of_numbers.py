def summ_nums(n):
	if n <= 0:
		return 0
	else:
		return n + summ_nums(n-1)


num = int(input('enter the number up to which \nto calculate the sum of the numbers '))
print(summ_nums(num))
