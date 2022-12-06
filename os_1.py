import os

file = 'admin.bat'
paper = 'access'

way_to_file = os.path.join('docs', paper, file)
print(way_to_file)
abs_way = os.path.abspath(file)
print(abs_way)


