# 5: Sales Spike Detection
sales = [1200, 1500, 900, 2200, 1400, 3000]
# Calculate the average daily sales.
avg_sales=sum(sales)/len(sales)
# Detect days where sales are more than 30% above average.
threshold=avg_sales*1.29
# Display the day number and sale value.
for i, sale in enumerate(sales):
    day_number=i+1
    if sale>=threshold:
        print(f"Day{day_number}:{sale}")