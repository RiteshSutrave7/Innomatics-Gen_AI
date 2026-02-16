# 6 Remove Duplicate Phone Numbers
phone_numbers = [9876543210, 9123456789, 9876543210]

# Converting a list to a set removes duplicates because sets only allow unique items
unique_phones = set(phone_numbers)

print(f"Unique phone numbers: {unique_phones}")