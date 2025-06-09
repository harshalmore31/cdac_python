
class Student_A10:
    _school_name = "Global Academy" 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def get_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    @classmethod
    def get_school_name(cls):
        return cls._school_name
    
    @classmethod
    def set_school_name(cls, new_school_name): 
        cls._school_name = new_school_name

    def display_details(self):
        grade = Student_A10.get_grade(self.marks)
        school = Student_A10.get_school_name()   

        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")
        print(f"School: {school}")

student_h_a10 = Student_A10("Harry", 85)
student_h_a10.display_details()

print("\nChanging school name for all students...")
Student_A10.set_school_name("Future Tech School")

student_i_a10 = Student_A10("Ivy", 92)
student_i_a10.display_details() 
student_h_a10.display_details() 
