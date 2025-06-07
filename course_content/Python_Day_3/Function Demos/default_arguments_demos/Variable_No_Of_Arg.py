 # variable number of arguments to a function

def disp(*vars):
	print("Type of vars is\t",type(vars))
	if(vars.__len__()==0):
		print("no argument passed")
	else:
		for k in vars:
			print(k)

def fun():
	disp()
	disp(10,20,30)
	disp("abc",200,True,3.4)
fun()
