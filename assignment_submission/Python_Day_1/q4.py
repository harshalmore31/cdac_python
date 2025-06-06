# Display numbers from 3 to 30 except number 24  using while loop.


print("Display numbers from 3 to 30 except number 24  using while loop.")

num = 3

while(num<30):
    num = num+1
    if num == 24:
        continue   # we are skipping the number : 24
    print(num)
