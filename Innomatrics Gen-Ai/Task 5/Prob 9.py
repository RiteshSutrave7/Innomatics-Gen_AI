# 9) E-Learning – Student Attendance Eligibility System
def check_exam_eligibility(attended_classes, total_classes):
    if total_classes == 0:
        attendance_percentage = 0.0
    else:
        attendance_percentage = (attended_classes / total_classes) * 100

    if attendance_percentage >= 75:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    print(f"Attendance Percentage: {attendance_percentage:.1f}")
    print(f"Exam Eligibility: {eligibility}")

print("Scenario 1: Eligible Student")
check_exam_eligibility(75, 100)
print();
print("Scenario 2: Not Eligible Student")
check_exam_eligibility(70, 100)
print();
print("Scenario 3: Borderline Eligible Student")
check_exam_eligibility(30, 40)
