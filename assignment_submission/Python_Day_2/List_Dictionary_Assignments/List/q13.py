items = [10, 20, 30, 40]
item = int(input("Enter item to find index: "))
if item in items:
    print("Index is:", items.index(item))
else:
    print("Item not found")