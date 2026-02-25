# 2) Online Food Delivery Time Estimator

def delivery_time(distance, traffic, weather):
    time = distance * 5
    if traffic.lower() == "high":
        time += 10
    elif traffic.lower() == "medium":
        time += 5
    if weather.lower() == "rainy":
        time += 5
    elif weather.lower() == "storm":
        time += 15
    print("Estimated Delivery Time:", time, "minutes")
    #input taken as
delivery_time(8, "High", "Rainy")