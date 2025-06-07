"""
Closure in Python is an inner function object, a function that behaves like an object, that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing.
"""

def outer():
    def inner():     # it's a closure
        print("inside inner function")
    print("inside outer function")
    return inner

var1=outer()
var1()

# place the breakpoint at both the print statements,debug and check the call stack