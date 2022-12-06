import os

def find_file(my_way, file_name):
	print('переходим в', my_way)
	for files in os.listdir(my_way):
		path = os.path.join(my_way, files)
		print('    смотрим', path)
		if file_name == files:
			return path
		if os.path.isdir(path):
			print('Это директория')
			result = find_file(path, file_name)
			if result:
				break
	else:
		result = None
	return result


file_path = find_file(os.path.abspath
					  (os.path.join('..', '..', 'setenses')),
					  'stivenson_105.py')
if file_path:
	print('Абсолютный путь до файла:', file_path)
else:
	print('Такого файла нет')



