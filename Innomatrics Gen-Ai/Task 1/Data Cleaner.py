# 3. Simple Data Cleaner

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

# Clean each name
for name in names:
    cleaned_name = name.strip().lower()  # Remove spaces & convert to lowercase
    cleaned_names.append(cleaned_name)

print("Cleaned Names:", cleaned_names)