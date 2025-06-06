# Write a program to accept a number and display its table

table = 10
num = int(input("Enter the number to get the table : \n"))
for i in range(table):
    mul = i*num
    print(f"{i} x {num} = {mul}")