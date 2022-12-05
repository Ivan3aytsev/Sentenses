a = {
	'h2': 'У нас самая низкая цена на iphone',
	'div': 'Купить',
	'p': 'продать'
}
for key in a:
	a[key] = a[key].replace('iphone', '00000000000000')
	print(a[key])
print(a)