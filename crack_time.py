def estimated_time_to_crack(password):
    pool_size = 0
    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(not char.isalnum() for char in password):
        pool_size += 32
    combinations = pool_size ** len(password)
    guesses_per_second = 10000000000
    seconds = (combinations / 2) / guesses_per_second
    if seconds < 1:
        return "Crakced in less than a second"
    elif seconds < 60:
        return f"Cracked in ~{int(seconds)} seconds"
    elif seconds < 3600:
        return f"Cracked in ~{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"Cracked in ~{int(seconds / 3600)} hours"
    elif seconds < 311040000:
        return f"Cracked in ~{int(seconds / 84600)} days"
    elif seconds < 311040000 * 1000:
        return f"Cracked in ~{int(seconds / 311040000)} years"
    else:
        return "Can't be cracked by brute-force"
