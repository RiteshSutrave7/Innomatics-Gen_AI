# 6) Password Strength Checker
print("# Password Strength Checker")
def check_password(password):
    special_chars = "@#$"

    has_digit = False
    has_special = False

    if len(password) < 8:
        return "Weak Password: Minimum length should be 8."

    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password: Must contain at least one digit and one special character (@#$)."


# Example
user_password = input("Enter password: ")
print(check_password(user_password))
