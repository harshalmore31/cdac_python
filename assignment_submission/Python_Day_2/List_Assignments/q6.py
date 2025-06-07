mylist = []

a, b, c, d, e = [int(x) for x in input("Enter five values: ").split()]
mylist += [a, b, c, d, e]

f = int(input("Enter the position to remove (0-4): "))

if 0 <= f < len(mylist):
    mylist.pop(f)
else:
    print("Invalid position!")

print("Updated List:", mylist)
print("Reversed List:", mylist[::-1])