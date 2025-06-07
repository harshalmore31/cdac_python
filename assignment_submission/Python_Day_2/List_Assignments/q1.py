mylist = []

name = input("Enter name: ")
number = int(input("Enter number: "))
flt = float(input("Enter float: "))

mylist = mylist + [name, number, flt]

new_name = input("Enter name to insert at 2nd position: ")
mylist.insert(1, new_name)

new_number = int(input("Enter another number: "))
mylist.append(new_number)

print("Final List:", mylist)