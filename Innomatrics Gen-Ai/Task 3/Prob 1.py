# 1: Employee Performance Bonus Eligibility
employees = {
"Ravi": 92,
"Anita": 88,
"Kiran": 92,
"Suresh": 85
}
# find the highest performance score
max_score=max(employees.values())
# find all employees with the highest score
top_performers=[name for name,score in employees.items() if score == max_score]
# format the names as a comma-separated string
names_string=",".join(top_performers)
# output the final result
print(f"Top performers Eligible for Bonus:{names_string}(Score:{max_score})")
