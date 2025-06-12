class Parent:
    def __init__(self):
        print("Parent constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1 constructor")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Child2 constructor")

c1 = Child1()
c2 = Child2()