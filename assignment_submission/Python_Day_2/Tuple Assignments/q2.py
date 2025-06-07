nums = tuple(int(x) for x in input("Enter 5 numbers separated by space: ").split())

asc = sorted(nums)
desc = sorted(nums, reverse=True)

print("Original Tuple:", nums)
print("Ascending Order:", asc)
print("Descending Order:", desc)