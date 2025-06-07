# global and local variable
var=500

def disp():
    print("value of var is\t",var)

def myfun():
    var=100
    print("value of var is\t",var)
    disp()
myfun()




