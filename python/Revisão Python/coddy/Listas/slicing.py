lst = input().split(",")
meio = len(lst) // 2
if len(lst) % 2 == 0:
    print(lst[meio - 1:meio + 1])
else:
    print(lst[meio - 1:meio + 2])