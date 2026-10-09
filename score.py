def password_length(password):
    if len(password) < 8:
        return 0
    elif len(password) < 10:
        return 4
    elif len(password) < 12:
        return 6
    elif len(password) < 16:
        return 8
    elif len(password) < 20:
        return 12
    elif len(password) < 25:
        return 18
    else:
        return 25
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

def bad_sequence(password):
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
                        return -2
        return 0

def no_leaked_passwords(password):
    leaked_passwords = [
     "123456", "password", "123456789", "qwerty", "12345678", "111111",
     "123123", "abc123", "password1", "iloveyou", "admin", "welcome", 
     "monkey", "dradon", "letmein", "87654321", "9876554321", "22222",
     "333333", "444444", "555555", "666666", "777777", "888888", "999999",
     "000000"    
    ]
    for seq in leaked_passwords:
        if seq in password.lower():
            return -2
    return 0


