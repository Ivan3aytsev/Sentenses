import os
project = 'sentenses'
print(os.path.abspath(project))
for i in os.listdir(project):
	path = os.path.join(project, i)
	print('   ', i)
print(os.getcwd())
# print(os.listdir(project))

# def find_name(key):
# 	if key in struct:
#         return struct[key]
#     for sub in struct.values():
#         if isinstance(sub, dict):
#             a = find_name(sub, key)
#             if a:
#                 break
#     else:
#         a = None
#     return a
#
#
# user_key = input('Искомый ключ: ')
# value = find_name(site, user_key)
# if value:
#     print(value)
# else:
#     print('такого ключа нет')