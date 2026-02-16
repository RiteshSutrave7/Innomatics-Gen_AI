# 4 Count Products Above a Price Threshold 

prices = [450, 1200, 899, 1500, 300]
count = 0

# Iterate through each price and check the condition
for price in prices:
    if price > 1000:
        count += 1

print(f"Products above 1000: {count}")