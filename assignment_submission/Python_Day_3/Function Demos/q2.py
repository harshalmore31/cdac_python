# 2) define a function which accepts a number and return its square.

def calculate_square(number):
    return number * number

num_for_square = int(input("Enter a number to get its square: "))
squared_value = calculate_square(num_for_square)
print(f"The square of {num_for_square} is {squared_value}.")


# 3) define a function which accepts character,int,string and display them.
def display_values(char_val, int_val, str_val):
    print(f"Character: {char_val}")
    print(f"Integer: {int_val}")
    print(f"String: {str_val}")
