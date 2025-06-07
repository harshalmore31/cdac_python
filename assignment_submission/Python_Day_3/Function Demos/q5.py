# 5) define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.

def check_number_sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

num_to_check_q5 = int(input("Enter a number to check its sign (positive, negative, or zero): "))
result_q5 = check_number_sign(num_to_check_q5)
print(f"The function returned: {result_q5}")
if result_q5 == 1:
    print(f"{num_to_check_q5} is positive.")
elif result_q5 == -1:
    print(f"{num_to_check_q5} is negative.")
else:
    print(f"{num_to_check_q5} is zero.")
