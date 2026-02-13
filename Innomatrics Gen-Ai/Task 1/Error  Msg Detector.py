# 5. Error Message Detector
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

# Count ERROR logs
for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR messages:", error_count)