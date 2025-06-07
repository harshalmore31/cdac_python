def myfun(*varg):
    print(type(varg))
    for i in varg:
        print(i)

myfun('A',"hello",5.6,True,500)

#    myfun(name="Rohit",age=30)     #    TypeError: myfun() got an unexpected keyword argument 'name'

print("\nlet's define keyworded argument function\n")
def myfun1(**varg):         # keyworded argument function
    print(type(varg))
    for key,value in varg.items():
        print(key,"\t",value)

myfun1(name="Rohit",age=30)
myfun1(name="Viraat",age=34,rollno=1,address="Mumbai")
# myfun1('A',100,"hello",6,7)  # must be key-value pair


