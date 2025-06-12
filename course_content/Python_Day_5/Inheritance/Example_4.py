# By default "object" is the parent class of all the classes

class Base:
    def __init__(self,num1):
        self.num1=num1
        print("Base class constructor")


class Sub(Base):
    def __init__(self,num2):
        super().__init__(num2+10)    # invoking parent class constructor explicitly
        self.num2=num2
        print("Sub class constructor")
       

s1 = Sub(100)
print(id(s1))
print(s1.num2)
print("\n")
print(s1.num1)

