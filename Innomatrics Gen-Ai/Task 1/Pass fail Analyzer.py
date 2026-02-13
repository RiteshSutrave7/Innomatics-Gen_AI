# -----------------------------------
# 2. Pass & Fail Analyzer
# -----------------------------------

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

# Analyze marks
for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Print results
print("Total Students:", len(marks))
print("Total Pass :", pass_count)
print("Total Fail:", fail_count)