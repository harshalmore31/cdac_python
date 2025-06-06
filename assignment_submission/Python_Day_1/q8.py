# accept a character and display whether it is upper case or lower case or not an alphabet

ch = input("Enter the character : ")
if ord(ch)>=65 and ord(ch)<=90:
    print(f"the char {ch} It is in upper case")
else:
    print(f"the char {ch}, It is in lower case")