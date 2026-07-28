num = float(input()) 
if num < 3.5:
    print(num)   
while num >= 3.5:
    num/= 2
    if num < 3.5:
        print(num)
        break
 