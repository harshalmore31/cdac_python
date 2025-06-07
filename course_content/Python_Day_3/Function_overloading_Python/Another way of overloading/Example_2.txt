from multipledispatch import dispatch

@dispatch(int,int)
def disp(val1,val2):
    print("Inside int method\t",val1,"\t",val2)

@dispatch(str,str)
def disp(val1,val2):
    print("Inside str method\t",val1,"\t",val2)

disp("hello","world")
disp(100,200)