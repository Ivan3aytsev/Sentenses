import os

direct = input('введите директорию ')
for files in os.listdir(direct):
	print(os.path.join(direct, files))

