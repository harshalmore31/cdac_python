mylist = []

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    mylist.append(num)

print("Numbers entered:", mylist)
print("Length of list:", len(mylist))