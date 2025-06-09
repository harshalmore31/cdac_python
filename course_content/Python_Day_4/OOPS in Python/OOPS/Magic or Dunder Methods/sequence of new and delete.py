class First:
    def __new__(cls):
        print("inside __new__ dunder method")
        instance=object.__new__(cls)
        print("id of instance is\t",id(instance))
        return instance
    def __init__(self):
        print("inside __init__ dunder method")

f1=First()
print("id of f1 is\t",id(f1))
print("\n")
print("done")