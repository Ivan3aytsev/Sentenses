def password1(word1):
	cap_sym = False
	small_sym = False
	number = False
	if len(word1) >= 8:
		for x in word1:
			if x.isalpha:
				if x.islower():
					small_sym = True
				else:
					cap_sym = True
			else:
				number = True
			if small_sym and number and cap_sym:
				return True
		else:
			return False
	else:
		return False

# def password2(word2):
# 	cap_sym = {chr(x) for x in range(65, 91)}
# 	small_sym = {chr(x) for x in range(97, 123)}
# 	number = {chr(x) for x in range(48, 58)}
# 	if len(word2) >= 8:
# 		for x in word2:
# 			if x in

word = input('введите пароль ')
print(password1(word))