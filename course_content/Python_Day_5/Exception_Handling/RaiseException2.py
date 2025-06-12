def double(var):
	if var<=0:
		raise Exception("IllegalValue Exception")
	return var*var

def fun():
	try:
		print(double(-4))
	except Exception as e:
		print("error is\t",e.__str__())
	print("Done")
fun()


# Output:

error is	 IllegalValue Exception
Done