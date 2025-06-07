mylist = []

a, b, c, d, e = [int(x) for x in input("Enter five values: ").split()]
mylist += [a, b, c, d, e]

f = int(input("Enter the number to delete: "))

if f in mylist:
    mylist.remove(f)
else:
    print(f, "is not in the list!")

print("Updated List:", mylist)
print("Reversed List:", mylist[::-1])