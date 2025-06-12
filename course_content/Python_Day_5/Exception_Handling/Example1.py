var=5
try:
    print(var/0)
except ZeroDivisionError:
    print("You can't devide any number by 0")
print("done")
