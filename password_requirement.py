
# Vad som får användas och vad som inte får användas

def no_space(password):
	if " " in password:
		return False
	return True

def no_sequence(password):
	bad_sequences = [
		"123", "234", "345", "456", "567", "678", "789", "890",
   		"321", "432", "543", "654", "765", "876", "987", "098",
		"abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij",
		"ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr",
		"qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
    		"cba", "dcb", "edc", "fed", "gfe", "hgf", "ihg", "jih",
		"kji", "lkj", "mlk", "nml", "onm", "pon", "qpo", "rqp",
		"srq", "tsr", "uts", "vut", "wvu", "xwv", "yxw", "zyx",
		"qwerty", "asdfgh", "zxcvbn", "qazwsx", "edcrfv", "aaa",
		"111", "bbb"
	]
	lowercase_password = password.lower()
	for seq in bad_sequences:
		if seq in lowercase_password:
			return False
	return True

def most_contain(password):
	uppercase = any(char.isupper() for char in password)
	lowercase = any(char.islower() for char in password)
	number = any(char.isdigit() for char in password)
	special_char = any(not char.isalnum() for char in password)
	return uppercase and lowercase and number and special_char

