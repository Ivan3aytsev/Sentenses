def fun(num, lst=None):
	lst = lst or []
	if not lst:
		lst = []
	lst.append(num)
	print('lst =', lst)


# n = int(input('num = '))
fun(5)
fun(10)
fun(15)