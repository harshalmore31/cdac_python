
class Employee_A9:
    company = "Infosys" # Class variable

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20 # 20% HRA
        da = self.basic_salary * 0.10  # 10% DA
        total_salary = self.basic_salary + hra + da
        return total_salary

    def display_info(self):
        total_salary = self.calculate_salary()
        print(f"Company: {Employee_A9.company}")
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: ${self.basic_salary:.2f}")
        print(f"Total Salary (Basic + HRA + DA): ${total_salary:.2f}")

emp_a9 = Employee_A9("Grace", 50000)
emp_a9.display_info()
