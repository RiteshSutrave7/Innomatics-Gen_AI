# 3) Agriculture – Rainfall Adequacy Checker
def check_rainfall(rainfall_list, required_level):
    total = 0

    for rain in rainfall_list:
        total += rain

    average = total / len(rainfall_list)

    if average >= required_level:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"

    print("Average Rainfall:", average)
    print("Rainfall Status:", status)

rain_data = [70, 80, 65, 75]
check_rainfall(rain_data, 70)