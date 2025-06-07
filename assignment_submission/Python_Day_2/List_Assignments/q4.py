a = int(input("Enter the number: "))
b = input("Enter the string: ")
c = input("Enter the boolean (True/False): ") == "True"
d = float(input("Enter the decimal: "))
e = input("Enter the character: ")

mylist = [a, b, c, d, e]

print("List (Normal Order):", mylist)
print("List (Reverse Order):", mylist[::-1])