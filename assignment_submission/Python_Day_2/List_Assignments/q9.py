names = [input(f"Enter name {i+1}: ") for i in range(5)]

ascending = sorted(names)
descending = sorted(names, reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)