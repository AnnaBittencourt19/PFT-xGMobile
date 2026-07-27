num1 = int(input())
num2 = int(input())
for i in range(num1, num2):
    if i % 2 == 0 and i > 5:
        print("First even number greater than 5:", i)
        break
for i in range(num1, num2):
    if i % 7 == 0:
        print("First number divisible by 7:", i)
        break