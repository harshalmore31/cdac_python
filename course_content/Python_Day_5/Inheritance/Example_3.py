class Base:
    def __init__(self):
        print("Base class constructor")


class Sub(Base):
    def __init__(self):
        super().__init__()    # invoking parent class constructor explicitly, can be on any line
        print("Sub class constructor")
       

s1 = Sub()
print(id(s1))
print(s1.__class__.__base__)
print(s1.__class__.__base__.__base__)
