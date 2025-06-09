
class Company_A7:
    company_name = "TechSoft" # Class variable

    def __init__(self, employee_name):
        self.employee_name = employee_name

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    def show_company_info(self):
        print(f"Employee '{self.employee_name}' works at {Company_A7.company_name}")
        
    


emp1_a7 = Company_A7("Fiona")
emp1_a7.show_company_info()

print("Changing company name using class method...")
Company_A7.change_company_name("Innovate Corp")

emp2_a7 = Company_A7("George")
emp1_a7.show_company_info() 
emp2_a7.show_company_info() 

