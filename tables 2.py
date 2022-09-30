def change(lst):
	lst[0], lst[-1] = lst[-1], lst[0]
	return lst


a = ['a', 't', 'p']
print(a)
print(change(a))