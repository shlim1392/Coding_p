def is_acceptable(password):
    vowels = "aeiou"
    
    has_vowel = any(char in vowels for char in password)
    if not has_vowel:
        return False

    for i in range(len(password) - 2):
        if all(c in vowels for c in password[i:i+3]) or all(c not in vowels for c in password[i:i+3]):
            return False

    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password[i:i + 2] not in ["ee", "oo"]:
            return False
    
    return True

while True:
    pw = input()
    if pw == "end":
        break
    
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
