# 1) Smart Parking Lot Management System

def smart_parking(capacity, logs):
    parked = 0
    peak_usage = 0
    for log in logs:
        if log == "IN":
            parked += 1
        elif log == "OUT":
            parked -= 1
        peak_usage = max(peak_usage, parked)
    print("Currently Parked Vehicles:", parked)
    if parked > capacity:
        print("Parking Status: Full - Capacity Exceeded")
    else:
        print("Parking Status: Available")
    print("Peak Parking Usage:", peak_usage)
#input taken as
smart_parking(50, ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"])
     