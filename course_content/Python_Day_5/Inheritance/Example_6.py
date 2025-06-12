# Method overriding

class Base:
    def __init__(self,num1):
        self.num1=num1
        print("Base class constructor ",self.num1)
    def disp1(self):       # overridden method
        print("Base class disp1 method")


class Sub(Base):
    def __init__(self):
        super().__init__(100)    # invoking Base class parameterized constructor explicitly
        print("Sub class constructor")

    def disp1(self):      #  overriding method
        super().disp1()    # explicitly invoking overridden method from overriding method
        print("Sub class disp1 method")


s1 = Sub()

s1.disp1()