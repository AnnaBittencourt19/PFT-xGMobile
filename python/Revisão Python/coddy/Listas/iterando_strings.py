text = input()
# Write your code below
count = 0
for char in text:
    char_conv = char.lower()
    if char_conv == 'p':
        count = count + 1
print(count)