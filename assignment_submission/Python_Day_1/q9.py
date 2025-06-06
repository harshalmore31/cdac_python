# display fibonicii series of 10 numbers

# def fibo(n):
#     if n
#     fx = fibo(n-1) + fibo(n-2)

# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34...........

# f2 = f1 + f2

# f1 = 1
# f2 = 1

num1 = 1
num2 = 1

print(f"{num1} \n{num2}")
for i in range(10):
    fibo = num1 + num2
    num1 = num2
    num2 = fibo
    print(fibo)

# def fibo(n):
    