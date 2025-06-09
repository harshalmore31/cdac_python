add=lambda x,y:x+y
print("add is the reference to the object of type\t",type(add))
print("address of the object where add refers to is\t", id(add))
print(add(5,6))

multiply=lambda x,y:x*y
print("multiply is the reference to the object of type\t",type(multiply))
print("address of the object where multiply refers to is\t", id(multiply))
print(multiply(9,8))

disp=lambda:print("welcome")
print("disp is the reference to the object of type\t",type(disp))
print("address of the object where disp refers to is\t", id(disp))
disp()


disp=lambda:[print("welcome"),print("hi"),print("Good Bye")]
print("disp is the reference to the object of type\t",type(disp))
print("address of the object where disp refers to is\t", id(disp))
disp()

# no need to collect lambda in any variable

(lambda:print("Welcome to lambda world"))()


print((lambda x: x*x)(10))





