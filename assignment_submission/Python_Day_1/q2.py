# Using switch ….case   display whether accepted character is vowel or not.

vowel = ["a","e","i","o","u"]

x = input("Enter the character to check whether its a vowel or not : ").lower()
if x in vowel:
    out = "Yes, it is a vowel"
    print(f"The character {x} is {out}")
else:
    out = "No, its not a vowel"
    print(f"The character {x} is {out}")
    
