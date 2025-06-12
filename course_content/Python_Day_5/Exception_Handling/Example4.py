
def fun():

	try:
		f=open("d:\\FileDemo1.java","r")
	except FileNotFoundError:
		print("File not Found")
	finally:
		print("I will always execute")
	print("Done")
fun()


