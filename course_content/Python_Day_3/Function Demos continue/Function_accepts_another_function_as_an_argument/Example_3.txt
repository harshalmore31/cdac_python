""" Python provides a built-in function, to determine which objects are callable. The function is callable(). 
If the object passed as a parameter to the callable() prints TRUE then that object is callable. 
If it displays FALSE then it is not callable in Python.
 """

def main(fun):
    if callable(fun):
        fun()
    else:
        print("You passed non-callable argument to main function")
    print("inside caller function")

def disp():
    print("inside disp function")

main(disp)    # works
temp=100
main(temp)    # you won't get TypeError


