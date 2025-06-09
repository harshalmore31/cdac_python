class MyClass:
    var=0
    def __init__(self,var):
        self.var=var
    def getvar(self):
        return self.var
    def __del__(self):
        print("No Reference is left for {}".format(self))

m1 = MyClass(10)
print(hex(id(m1)))
print(m1.getvar())
m1 = MyClass(10)
print(hex(id(m1)))
print(m1.getvar())
print("done")

