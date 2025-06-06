# accept a number and display whether it is prime or not
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    for j in range(2, num):
        if num % j == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")