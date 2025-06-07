# 1) accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.

student_dict = {}
print("Enter 5 student names:")
for i in range(1, 6):
    name = input(f"Enter name for student {i}: ")
    student_dict[i] = name
print("Student Dictionary:", student_dict)
print("-" * 20)
