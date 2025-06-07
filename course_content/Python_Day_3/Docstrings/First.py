# creating and accessing "docstring" for user defined functions

def square(num):
    ''' this function accepts a number and return its square '''
    return num*num

print(square(10))
print(square.__doc__)