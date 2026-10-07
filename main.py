import score
import password_requirement
total_score = 0
user_password = input("Enter your password here: ")

if not password_requirement.most_contain(user_password):
	print("Most contain Uppercase, lowercase, number and special character")
if not password_requirement.no_space(user_password):
	print("Can not contain spaces")
if not password_requirement.no_sequence(user_password):
	print("Can not contain sequences")

total_score += score.password_length(user_password)
total_score += score.number(user_password)
total_score += score.special_character(user_password)
total_score += score.uppercase(user_password)
total_score += score.lowercase(user_password)

print(total_score)
