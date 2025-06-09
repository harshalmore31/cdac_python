item_name = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price per item: "))

total = quantity * price

print(f"You bought {quantity} {item_name}(s) at ₹{price} each. Total cost is ₹{total}.")