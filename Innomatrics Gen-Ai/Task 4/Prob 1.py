#  1) Mobile Recharge Validation System
print("# Mobile Recharge Validation System")

def validate_recharge(amount):
    valid_plans = [199, 299, 399, 599]

    if amount < 50:
        print("Recharge amount must be at least ₹50.Valid plans: 199, 299, 399, 599")
        return False
    elif amount not in valid_plans:
        print("Invalid plan selected. Valid plans: 199, 299, 399, 599")
        return False
    else:
        print("Recharge successful!")
        return True


# Retry using while loop
while True:
    try:
        recharge_amount = int(input("Enter recharge amount: "))
        if validate_recharge(recharge_amount):
            break
    except ValueError:
        print("Please enter a valid number.")
     