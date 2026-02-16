# 7 Count Character Frequency 
text = "pythonp"
freq = {}

for char in text:
    # .get(char, 0) looks for the char; if not found, it starts at 0
    freq[char] = freq.get(char, 0) + 1

print(freq)