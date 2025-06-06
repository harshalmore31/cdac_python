# display prime numbers from 3 to 30

for i in range(3,30):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)

