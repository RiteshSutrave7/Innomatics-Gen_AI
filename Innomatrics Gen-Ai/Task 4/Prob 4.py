# 4)Cab Fare Estimator with Retry Option
print("# Cab Fare Estimator with Retry Option")
def calculate_fare(distance, is_peak):
    base_fare = 50
    fare = base_fare + (12 * distance)

    # Add 25% extra during peak hours
    if is_peak:
        fare += fare * 0.25

    return fare


# Retry loop
while True:
    try:
        distance = float(input("Enter distance in km: "))

        if distance <= 0:
            print("Distance must be greater than 0.")
            continue

        peak_input = input("Is it peak hour? (yes/no): ").lower()

        if peak_input == "yes":
            total_fare = calculate_fare(distance, True)
        elif peak_input == "no":
            total_fare = calculate_fare(distance, False)
        else:
            print("Invalid input for peak hour. Please enter yes or no.")
            continue

        print(f"Total Fare: ₹{total_fare:.2f}")

        # Ask user if they want to retry
        retry = input("Do you want to calculate again? (yes/no): ").lower()

        if retry != "yes":
            print("Thank you for using Cab Fare Estimator!")
            break

    except ValueError:
        print("Invalid input. Please enter numeric value for distance.")
     