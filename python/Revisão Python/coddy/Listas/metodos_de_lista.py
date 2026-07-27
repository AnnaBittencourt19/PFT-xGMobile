def merge(lst1, lst2):
    # Write code here
    final = []
    for i in range(len(lst1)):
        final.append(lst1[i]) 
    for i in range(len(lst2)):
        final.append(lst2[i])
    final.sort()
    return final

