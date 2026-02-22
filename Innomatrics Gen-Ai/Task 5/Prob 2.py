# 2) Healthcare – Medicine Stock Alert System
def check_medicine_stock(stock):
    if stock < 10:
        status = "Low Stock Alert"
    else:
        status = "Stock Sufficient"

    print("Medicine Stock:", stock)
    print("Status:", status)


check_medicine_stock(6)