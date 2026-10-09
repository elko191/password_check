import score
import forbidden
import crack_time

while True:
    user_password = input("Enter your password here: ")
    
    if user_password.lower() == "exit":
        print("Program closed")
        break
        
    if not forbidden.forbidden_characters(user_password):
         print("Can not use Spases, ', ¸¸\", \\")
    else:    
        total_score = 0
        total_score += score.password_length(user_password)
        total_score += score.number(user_password)
        total_score += score.special_character(user_password)
        total_score += score.uppercase(user_password)
        total_score += score.lowercase(user_password)
        total_score += score.bad_sequence(user_password)
        total_score += score.no_leaked_passwords(user_password)
        time_to_crack = crack_time.estimated_time_to_crack(user_password)

    
        if total_score <= 10:
	        print("\033[31mNot Secure\033[0m")
        elif total_score <= 16:
	        print("\033[33mSecure\033[0m")
        else:
	        print("\033[32mVery secure\033[0m")
        print(time_to_crack)
        print("-" * 40)
    
