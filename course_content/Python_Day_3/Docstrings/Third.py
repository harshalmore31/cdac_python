# creating and accessing multiline docstring


def myfun():
    """ 
    this is myfun 
    it prints hello message
    it is a special function
    """
    print("Hello")

myfun()
print(myfun.__doc__)