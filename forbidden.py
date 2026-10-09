def forbidden_characters(password):
	if " " in password:
		return False
	if "'" in password:
		return False
	if '"' in password:
		return False
	if "\\" in password:
		return False
	return True

