# Global Variable and Local variable
var=500  # global variable

def disp():
   return var  # global var

def myfun():
    var=100  # local variable
    print("var inside main\t",var) # by default local is given precedence
    print("global var is\t",disp())
myfun()


