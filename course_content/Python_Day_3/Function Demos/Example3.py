# Global Variable and Local variable
var=500
def myfun():
    val=100
    print("var inside main\t"+str(var))
    print("val inside main\t"+str(val))
myfun()

def disp1():
    print("var inside disp1\t"+str(var))
  #   print("val inside disp1\t"+str(val))  cannot access val
disp1()