# def password1(word1):
# 	cap_sym = False
# 	small_sym = False
# 	number = False
# 	if len(word1) >= 8:
# 		for x in word1:
# 			if x.isalpha:
# 				if x.islower():
# 					small_sym = True
# 				else:
# 					cap_sym = True
# 			else:
# 				number = True
# 	else:
# 		return False
# 	if small_sym and number and cap_sym:
# 		return True
# 	else:
# 		return False

def password_2(word_2):
	cap_sym = {chr(x) for x in range(65, 91)}
	small_sym = {chr(x) for x in range(97, 123)}
	number = {chr(x) for x in range(48, 58)}
	cap = False
	small = False
	num = False
	if len(word_2) >= 8:
		for x in word_2:
			if not num and x in number:
				num = True
			elif not cap and x in cap_sym:
				cap = True
			elif not small and x in small_sym:
				small = True
			elif small and cap and num:
				return True
		else:
			return False
	else:
		return False


# word = input('введите пароль ')
# print(password1(word))


for _ in range(15):
	word = input('введите пароль ')
	print(password_2(word))
