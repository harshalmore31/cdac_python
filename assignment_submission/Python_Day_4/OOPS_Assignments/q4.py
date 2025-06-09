
class Employee_A4:
    def __init__(self, name):
        self.name = name
        print(f"Employee '{self.name}' created")

    def __del__(self):
        # This is the destructor
        print(f"Employee '{self.name}' destroyed")

emp_obj_a4 = Employee_A4("Harshal")
print("Employee object 'emp_obj_a4' exists.")

print("Deleting emp_obj_a4...")

