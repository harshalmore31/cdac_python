class Test:
    x=10
    def __init__(self,a,b):
        self.a=a
        self.b=b

ref=Test   #  "ref"  refers to class object
print(dir(ref))    #  observe that "x" is a member of class object because it's a static member
ref1=Test  #  "ref1" refers to class object
print("\n")
print(id(ref)==id(ref1))   # true , as class object is one only and both "ref" and "ref1" refer to the same class object
t1=Test(10,20)  # instance object
t2=Test(30,40)  # instance object
print("\n")
print(dir(t1))   #  a and b also will be displayed
print("\n")
print(id(t1)==id(t2))   #  false