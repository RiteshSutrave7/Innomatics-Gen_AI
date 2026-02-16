# 2 Highest Salary from Employee Data
employees = {"Ravi": 75000, "Anita": 68000, "Kiran": 72000}

# Get the key with the maximum value
highest_paid = max(employees, key=employees.get)

print(f"Highest Salary: {highest_paid} - {employees[highest_paid]}")