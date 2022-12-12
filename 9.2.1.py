import os

way = input('введите путь до файла ')
if os.path.exists(way):
	if os.path.isdir(way):
		print('ЭТО ДИРЕКТОРИЯ')
	elif os.path.isfile(way):
		print(f'ЭТО ФАЙЛ\nразмер файла: {os.path.getsize(way)} байт')
	elif os.path.islink(way):
		print('это ссылка')

else:
	print('\nфайла по такому пути не существует')