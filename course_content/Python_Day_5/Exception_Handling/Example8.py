
def fun():
	try:
		f=open("d:\\FileDemo.java","r")
		for content in f:
			print(content)
		var=10/0
	except Exception as e:
		print("some other error\t",e)
	except ZeroDivisionError as z:
		print("error is\t",z)
	print("Done")
fun()


