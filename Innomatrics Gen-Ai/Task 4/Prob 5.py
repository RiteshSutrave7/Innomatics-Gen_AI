# 5) Attendance Eligibility Checker
print("# Attendance Eligibility Checker")
def check_attendance(attendance_list):
    present_days = 0

    for day in attendance_list:
        if day == "P":
            present_days += 1

    percentage = (present_days / len(attendance_list)) * 100

    if percentage >= 75:
        return f"Attendance: {percentage:.2f}% - Eligible"
    else:
        return f"Attendance: {percentage:.2f}% - Not Eligible"


# Example
attendance = ["P", "A", "P", "P", "A", "P", "P", "P"]
result = check_attendance(attendance)
print(result)
     