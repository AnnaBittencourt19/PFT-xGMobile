lst = list(map(int, input().split(",")))
# Write your code below
lst_if = []
for index, numero in enumerate(lst):
    if numero < 50 or (numero % 5) == 0:
        lst_if.append(index)
print(lst_if)
