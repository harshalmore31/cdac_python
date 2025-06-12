# how to write inside a file
with open("myfile.txt","w") as f:
	print("enter messages, stop to quit\n")
	while True:
		str=input()
		if str=="stop":
			break
		f.writelines(str+"\n")

print("Done")

