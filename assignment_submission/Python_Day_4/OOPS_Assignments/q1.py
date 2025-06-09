
class Student_A1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

student1_a1 = Student_A1("Harshal", 20)
student2_a1 = Student_A1("Utkarsh", 22)

print("Details of student 1:")
student1_a1.display()
print("Details of student 2:")
student2_a1.display()
