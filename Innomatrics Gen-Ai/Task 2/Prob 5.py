# 5 Calculate Attendance Percentage 
attendance = ["P", "P", "A", "P", "P"]
present_days = attendance.count("P")
percentage = (present_days / len(attendance)) * 100

print(f"Attendance Percentage: {percentage}")