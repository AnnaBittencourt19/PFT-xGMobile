def reverse(lst):
    # Write code here
    nova_list = []
    for i in range(len(lst)):
        nova_list.append(lst[len(lst)-i-1])
    return nova_list