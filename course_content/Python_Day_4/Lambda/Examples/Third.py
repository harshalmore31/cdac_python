def myfun(fun,num):
    fun(num)
disp=lambda x: [print(i) for i in range(1,x)]

myfun(disp,7)