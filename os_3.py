import os


def find_file(my_way, file_name):
	print('переходим в', my_way)
	# if os.path.exists(file_name):
	result_list = []
	for files in os.listdir(my_way):
		path = os.path.join(my_way, files)
		print('    смотрим', path)
		if file_name in files:
			result_list.append(files)
		if os.path.isdir(path):
			print('Это директория')
			find_file(path, file_name)
	return result_list
	# else:
	# 	print('такого файла не существует')


file_n = 'h3hota'
	# input('название искомого файла: ')
way = 'C:\Games\HoMM v3.5'
	# input('введите путь до папки, в которой надо сделать поиск ')
file_path = find_file(way, file_n)
if file_path:
	print('\n')
	print(f'найдено {len(file_path)} файлов')
	for ways in file_path:
		print('Абсолютный путь до файла:', ways)
else:
	print('Такого файла нет')
