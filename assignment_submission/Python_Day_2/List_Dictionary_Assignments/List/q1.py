nums = [10, 45, 32, 60, 25, 90]
threshold = int(input("Enter the number: "))
result = [x for x in nums if x > threshold]
print("Numbers greater than", threshold, ":", result)