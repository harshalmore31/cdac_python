# passing lambda as an argument

def myfun(fun):
    fun()
temp=lambda:print("welcome to lambda world")
myfun(temp)

myfun(lambda:print("this is another lambda"))