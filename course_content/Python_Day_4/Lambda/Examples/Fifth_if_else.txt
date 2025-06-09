temp1=lambda *x:[print("no arg passed to lambda") if(len(x)==0)  else [print(i) for i in x ]]
temp1()
temp1(300)
temp1(500,600)

min = lambda a, b : a if(a < b) else b
print(min(100, 20))

min1 = (lambda a, b : a if(a < b) else b)(10,20)
print(min1)