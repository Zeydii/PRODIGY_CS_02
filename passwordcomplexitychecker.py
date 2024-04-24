import re

def check_password_complexity(password):
    length_score = len(password) >= 8  # Minimum length requirement
    lowercase_score = any(char.islower() for char in password)
    uppercase_score = any(char.isupper() for char in password)
    digit_score = any(char.isdigit() for char in password)
    special_char_score = bool(re.match('^[\w@#$%^&+=]*$', password))  # Checking for special characters

    score = sum([length_score, lowercase_score, uppercase_score, digit_score, special_char_score])

    return score

def main():
    password = input("Enter your password: ")
    complexity_score = check_password_complexity(password)

    if complexity_score == 5:
        print("Password strength: Strong")
    elif complexity_score >= 3:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

main()