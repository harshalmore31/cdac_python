def myfun(fun,*val):
    fun(val)

multiple=lambda *arg:[print(i) for i in arg]

myfun(multiple,10,20,30,40,50)