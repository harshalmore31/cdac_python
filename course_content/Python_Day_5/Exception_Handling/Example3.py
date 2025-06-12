print("Let's open a file")
try:
    open("d:\\sample1.txt","r")
except FileNotFoundError:
    print("File not found")
print("done")
