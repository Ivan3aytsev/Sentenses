def checkPassword(password):
	has_upper = False
	has_lower = False
	has_num = False
	for ch in password:
		if "A" <= ch <= "Z":
			has_upper = True
		elif "a" <= ch <= "z":
			has_lower = True
		elif "0" <= ch <= "9":
			has_num = True
	if len(password) >= 8 and has_upper and has_lower and has_num:
		return True
	return False


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
	print(checkPassword(word))
