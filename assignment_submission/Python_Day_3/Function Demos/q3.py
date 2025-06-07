# 3) define a function which accepts character,int,string and display them.

def display_values(char_val, int_val, str_val):
    print(f"Character: {char_val}")
    print(f"Integer: {int_val}")
    print(f"String: {str_val}")

sample_char = 'A'
sample_int = 123
sample_string = "Hello Python"
print("Displaying sample values using the function:")
display_values(sample_char, sample_int, sample_string)
