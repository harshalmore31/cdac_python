# 6) define a function which accepts a character and return toggle of it.

def toggle_char_case(character):
    if 'a' <= character <= 'z':
        # Convert to uppercase: ASCII value of 'a' is 97, 'A' is 65. Difference is 32.
        return chr(ord(character) - 32)
    elif 'A' <= character <= 'Z':
        # Convert to lowercase:
        return chr(ord(character) + 32)
    else: # if not an alphabet character
        return character # return as is
    

char_input_q6 = input("Enter a single character to toggle its case: ")
if len(char_input_q6) == 1:
    toggled_char = toggle_char_case(char_input_q6)
    print(f"Original character: '{char_input_q6}', Toggled character: '{toggled_char}'")
else:
    print("Please enter only a single character.")
