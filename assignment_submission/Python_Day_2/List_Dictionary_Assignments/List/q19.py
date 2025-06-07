def common_member(list1, list2):
    return bool(set(list1) & set(list2))

l1 = [1, 2, 3]
l2 = [4, 5, 3]

print("Common member exists:", common_member(l1, l2))