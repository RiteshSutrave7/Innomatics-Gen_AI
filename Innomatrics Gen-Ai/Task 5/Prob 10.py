# 10) Smart Electricity Bill Analyzer
def calculate_electricity_bill(units_consumed):
    total_bill = 0
    usage_status = ""
    if units_consumed <= 100:
        total_bill = units_consumed * 3
    elif units_consumed <= 200:
        total_bill = (100 * 3) + ((units_consumed - 100) * 5)
    else:
        total_bill = (100 * 3) + (100 * 5) + ((units_consumed - 200) * 7)
    if total_bill < 500:
        usage_status = "Low Usage"
    elif 500 <= total_bill <= 1500:
        usage_status = "Moderate Usage"
    else:
        usage_status = "High Usage"

    print(f"Units Consumed: {units_consumed}")
    print(f"Total Bill: ₹{total_bill:.2f}")
    print(f"Usage Status: {usage_status}")
print("Scenario 1: Low Usage (50 units)")
calculate_electricity_bill(50)
print();
print("Scenario 2: Moderate Usage (150 units)")
calculate_electricity_bill(150)
print();
print("Scenario 3: High Usage (300 units)")
calculate_electricity_bill(300)
print();
print("Scenario 4: Borderline Low Usage (166 units -> 300 + 330 = 630)")
calculate_electricity_bill(166)
print();
print("Scenario 5: Borderline High Usage (200 units -> 300 + 500 = 800)")
calculate_electricity_bill(200)