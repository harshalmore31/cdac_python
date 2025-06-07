# 2) define nested function and show how will you invoke it.


def outer_function():
    print("Inside outer_function - starting.")

    message = "This message is from outer_function."

    def inner_function():
        print("  Inside inner_function - starting.")
        print(f"  Inner function says: {message}")
        print("  Inside inner_function - ending.")

    # To invoke the nested function, you call it from within the outer function's scope,
    # after it has been defined.
    print("Outer_function is now going to call inner_function.")
    inner_function()

    print("Outer_function has finished calling inner_function.")
    print("Inside outer_function - ending.")

# Demonstrating the invocation of the nested function
print("Calling outer_function to demonstrate nested function invocation:")
outer_function()

