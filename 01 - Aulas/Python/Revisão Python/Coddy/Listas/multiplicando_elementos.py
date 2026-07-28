def prod(lst):
    # Write code here
    mult = 1
    for i in range(len(lst)):
        mult *= lst[i] 
    return mult
