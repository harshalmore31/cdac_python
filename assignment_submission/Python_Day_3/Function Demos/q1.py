# 1) define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

def add():
    print("Add function called.")

def modify():
    print("Modify function called.")

def delete():
    print("Delete function called.")

user_choice_q1 = input("Enter a number (1 for add, 2 for modify, 3 for delete): ")
if user_choice_q1.isdigit(): # Basic check to see if input is a digit
    choice_num_q1 = int(user_choice_q1)
    match choice_num_q1:
        case 1:
            add()
        case 2:
            modify()
        case 3:
            delete()
        case _: # Default case for other numbers
            print("Invalid choice. Please enter 1, 2, or 3.")
else:
    print("Invalid input. Please enter a number.")
