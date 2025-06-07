mylist = []

a, b, c, d, e = [int(x) for x in input("Enter five values: ").split()]

mylist += [a, b, c, d, e]
print("Initial List:", mylist)

mylist.extend([100, 200, 300])
print("After Extending:", mylist)