lst = [10, 20, 30]
n = int(input("Enter index to check: "))
if 0 <= n < len(lst):
    print(f"Element at index {n} is {lst[n]}")
else:
    print("Index does not exist")