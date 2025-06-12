
def fun():

	try:
		f=open("d:\\FileDemo.java","r")
	except FileNotFoundError:
		print("File not Found")
	finally:
		print("I will always execute")
	print("Done")
fun()


