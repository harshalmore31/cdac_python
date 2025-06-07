# 1) create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
# invoke caller function by passing show1,show2 and show3

def show1():
    print("This is show1() function.")

def show2():
    print("This is show2() function.")

def show3():
    print("This is show3() function.")

def caller(function_to_be_called):
    print(f"Caller function received a function. About to call it...")
    function_to_be_called()
    print("Caller function has finished invoking the passed function.")
    print("---")


print("Invoking caller with show1:")
caller(show1)

print("Invoking caller with show2:")
caller(show2)

print("Invoking caller with show3:")
caller(show3)


