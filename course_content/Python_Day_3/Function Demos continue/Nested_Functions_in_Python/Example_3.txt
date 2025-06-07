"""

The inner function maintains a reference to the variables in the scope of "outer" through closure, allowing it to access "num" even after outer has finished executing.

The closure mechanism keeps the environment of "outer" function alive in memory as long as there's a reference to the "inner" function.

"""


def outer():
    num=100
    def inner():     # it's a closure
        print("inside inner function\t",num)
    num=400
    print("inside outer function")
    return inner

var1=outer()
var1()