# By default "object" is the parent class of all the classes
class MyClass:
    def __init__(self,num):
        self.num=num


m1 = MyClass(10)
print(type(m1))
print(m1.__dict__)
print(m1.__class__)
print(m1.__class__.__base__)