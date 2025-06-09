# a) Normal function with default argument
def display_args(arg1, arg2="Default"):
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)

# Example usage
display_args("Hello")
display_args("Hello", "World")

# b) Lambda function with default argument
display_lambda = lambda arg1, arg2="Default": print("Argument 1:", arg1, "\nArgument 2:", arg2)

# Example usage
display_lambda("Hello")
display_lambda("Hello", "World")