
from special.Arithmetic import add, multiply, subtract
from special.Display import wish

print("Demonstrating functions from the 'special' package")


num1 = 10
num2 = 5

sum_result = add(num1, num2)
product_result = multiply(num1, num2)
difference_result = subtract(num1, num2)

print(f"\n--- Arithmetic Operations ---")
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
print(f"The difference between {num1} and {num2} is: {difference_result}")

user_name = "Alice"
welcome_message = wish(user_name)

print(f"\nDisplay")
print(welcome_message)



