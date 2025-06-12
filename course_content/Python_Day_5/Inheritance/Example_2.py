# constructor overriding in Python

class Base:
    def __init__(self):
        print("Base class constructor")


class Sub(Base):
    def __init__(self):       # since this is available , init of Base won't be invoked when we instantiate Sub
        print("Sub class constructor")
       

s1 = Sub()
print(id(s1))
print(s1.__class__.__base__)
print(s1.__class__.__base__.__base__)
