# generic catch block

def fun():
	try:
		f=open("d:\\FileDemo.java","r")
		for content in f:
			print(content)
		var=10/0
	except Exception as e:
		#print("some other error\t",e.__str__())
		print("some other error\t",e)
	print("Done")
fun()


