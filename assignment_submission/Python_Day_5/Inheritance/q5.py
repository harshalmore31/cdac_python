class Base:
    def __init__(self, x):
        print("Base constructor with:", x)

class Sub(Base):
    def __init__(self, x, y):
        super().__init__(x)  
        print("Sub constructor with:", y)

s = Sub(10, 20)