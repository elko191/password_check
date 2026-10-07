def password_length(password):
	if len(password) < 8:
		return 0
	elif len(password) >= 8 and len(password) < 10:
		return 4
	elif len(password) >= 10 and len(password) < 12:
		return 6
	elif len(password) >= 12 and len(password) < 16:
		return 8
	else:
		return 15

def number(password):
	if any(char.isdigit() for char in password):
		return 2
	return 0

def special_character(password):
	for char in password:
		if not char.isalnum():
			return 2
	return 0

def uppercase(password):
	for char in password:
		if char.isupper():
			return 2
	return 0

def lowercase(password):
	for char in password:
		if char.islower():
			return 2
	return 0


