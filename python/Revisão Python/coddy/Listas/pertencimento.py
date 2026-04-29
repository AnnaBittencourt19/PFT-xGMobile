lst1 = input().split(",")
lst2 = input().split(",")
lst3 = []
# Write your code below
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print(lst3)
