# 6) Agriculture – Premium Crop Price Filter
def filter_premium_crops(prices):
    premium = []

    for price in prices:
        if price > 2000:
            premium.append(price)

    print("Premium Crops:", premium)

crop_prices = [1500, 2500, 1800, 3200]
filter_premium_crops(crop_prices)