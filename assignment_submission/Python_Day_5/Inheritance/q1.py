class GrandParent:
    def __init__(self):
        print("GrandParent constructor")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  
        print("Child constructor")

c = Child()