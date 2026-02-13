# -----------------------------------
# 1. User Login Check
# -----------------------------------

# Stored credentials
r_username = "admin"
r_password = "1234"

# Given credentials (can be replaced with input() if needed)
username = "admin"
password = "1234"

# Check login
if username == r_username and password == r_password:
    print("Login Successful")
else:
    print("Invalid Credentials")
    