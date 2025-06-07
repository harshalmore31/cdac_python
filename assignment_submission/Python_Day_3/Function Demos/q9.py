# 9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]


def sum_all_values(*numbers): # *numbers collects all positional arguments into a tuple called 'numbers'
    current_sum = 0
    if not numbers: # Check if no arguments were passed
        print("No numbers provided to sum.")
        return 0 # Or handle as appropriate

    print("Numbers received:", numbers)
    for num in numbers:
        current_sum += num
    return current_sum

sum1 = sum_all_values(1, 2, 3)
print(f"Sum (1, 2, 3): {sum1}")

sum2 = sum_all_values(10, 20, 30, 40, 50)
print(f"Sum (10, 20, 30, 40, 50): {sum2}")

sum3 = sum_all_values(5)
print(f"Sum (5): {sum3}")

sum4 = sum_all_values() # Calling with no arguments
print(f"Sum (no arguments): {sum4}")
