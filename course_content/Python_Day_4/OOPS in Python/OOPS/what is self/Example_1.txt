class First:
    def mainfunction(self):
        print("address of self is\t",id(self))
        print("type of self is\t",type(self))
        print("inside main function")
f1=First()
print("address of f1 is\t",id(f1))
f1.mainfunction()

f2=First()
print("address of f2 is\t",id(f2))
print("let's invoke mainfunction with f2")
f2.mainfunction()
