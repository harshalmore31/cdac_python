myset = set()

print("Enter 10 values:")
for i in range(10):
    val = input(f"Enter value {i+1}: ")
    myset.add(val)

print("Initial Set:", myset)

to_remove = input("Enter a value to remove from set: ")

myset.discard(to_remove)  

print("Final Set:", myset)