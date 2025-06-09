X = int(input("Enter the number to get square:"))
#a) Normal func
def square(X):
    print(X ** 2)

# b) lambda func
square = lambda X : X ** 2

print(square(X))