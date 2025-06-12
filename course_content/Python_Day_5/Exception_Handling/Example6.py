
def fun():

	try:
		f=open("d:\\FileDemo1.java","r")
	finally:
		print("I will always execute")
	print("Done")
fun()


