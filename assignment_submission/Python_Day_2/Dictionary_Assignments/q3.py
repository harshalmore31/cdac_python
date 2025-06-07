# 3) define a class "Student" with members
# 	name,age,address and qualification
	
#    define parameterized constructor and "str" member function which returns all the members

#    create 4 objects of Student by passing values.

# now create a dictionary with rollno ( start from 1 ) as a key and student object as a value.

# accept a rollno from user and display all its details i.e. name,age,address and qualification.
# also display message "student not found" in case if rollno entered by user is not available as a key inside the dictionary.


class Student:
    def __init__(self, name, age, address, qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}, Qualification: {self.qualification}"

student1 = Student("Harshal More", 20, "Mumbai", "Computer Science")
student2 = Student("Jayraj Sawant", 20, "Mumbai", "Mathematics")
student3 = Student("Utkarsh Singh", 20, "Mumbai", "Physics")
student4 = Student("Himanshu Shinde", 20, "Mumbai", "Chemistry")

students_dict = {
    1: student1,
    2: student2,
    3: student3,
    4: student4
}

rollno = int(input("Enter roll number: "))

if rollno in students_dict:
    print(students_dict[rollno])
else:
    print("student not found")