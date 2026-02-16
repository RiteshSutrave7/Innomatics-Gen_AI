# 3 Find Maximum and Minimum Values
numbers = [45, 22, 89, 10, 66]

# Initialize both with the first number in the list
max_val = min_val = numbers[0]

for num in numbers:
    # If current number is larger than our stored max, update max
    if num > max_val:
        max_val = num
    # If current number is smaller than our stored min, update min
    if num < min_val:
        min_val = num

print(f"Max: {max_val}\nMin: {min_val}")