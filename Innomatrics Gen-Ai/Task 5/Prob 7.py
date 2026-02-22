# 7) System Monitoring – Application Health Checker
def check_application_health(error_count):
    if error_count == 0:
        status = "Healthy"
    elif error_count <= 5:
        status = "Minor Issues"
    else:
        status = "Critical Issues"

    print("Error Count:", error_count)
    print("System Status:", status)

check_application_health(7)