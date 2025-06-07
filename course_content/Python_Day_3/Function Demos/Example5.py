# Global Variable and Local variable
var=500  # global variable
def myfun():
    var=100  # local variable
    print("var inside main\t",var) # by default local is given precedence
myfun()

def disp():
    print("var inside disp\t",var)
disp()
