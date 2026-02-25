# 4) Cloud Server Load Classification System

def server_load(cpu_readings):
    avg_cpu = sum(cpu_readings) / len(cpu_readings)
    if avg_cpu < 50:
        status = "Normal"
    elif avg_cpu <= 80:
        status = "Warning"
    else:
        status = "Critical"
    print(f"Average CPU Load: {int(avg_cpu)}%")
    print("Server Status:", status)
server_load([45, 60, 70, 85, 90]) #CPU readings