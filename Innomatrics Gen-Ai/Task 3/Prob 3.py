# 3: Sensor Data Validation
sensor_readings = [3, 4, 7, 8, 10, 12, 5]
# Identify readings that are even numbers (valid readings).
valid_readings=[]
# Store them as (hour_index, reading_value) pairs.
for hour_index,reading_value in enumerate(sensor_readings):
    # Ignore odd readings (invalid readings).
    if reading_value % 2 == 0:
        # if even append the(hour,value)tuple to the valid list
        valid_readings.append((hour_index,reading_value))
print("Valid Sensor Readings (Hour,Value:",valid_readings)