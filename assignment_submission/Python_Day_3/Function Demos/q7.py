# 7) define a function which accepts a string , toggle and return it.
#	[ hint :  use "swapcase()" function of string ]

def toggle_string_case(input_string):
    return input_string.swapcase()

string_input_q7 = input("Enter a string to toggle its case: ")
toggled_string = toggle_string_case(string_input_q7)
print(f"Original string: '{string_input_q7}'")
print(f"Toggled string: '{toggled_string}'")

