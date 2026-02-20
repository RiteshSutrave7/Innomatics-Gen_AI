# 3) Student Result Processing System
print("# Student Result Processing System")
def process_result(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 50:
        return f"Average: {average:.2f} - Pass"
    else:
        return f"Average: {average:.2f} - Fail"


# Example
student_marks = [60, 70, 45, 55]
result = process_result(student_marks)
print(result)
     