words = ['python', 'java', 'c', 'cplusplus', 'go']
n = int(input("Enter the minimum length: "))
result = [word for word in words if len(word) > n]
print("Words longer than", n, ":", result)