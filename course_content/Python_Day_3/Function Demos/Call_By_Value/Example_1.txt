# call by value concept
def change(var):
    print("id of var before changing var is\t",id(var))
    var+=1
    print("Value of var is\t",var)
    print("id of var after changing var is\t",id(var))
num=10
print("id of num is\t",id(num))
print("before\t",num)
change(num)
print("after\t",num)
