# multilevel inheritance

class Base:
    def disp1(self):
        print("Base class disp1")


class Sub1(Base):
    def disp2(self):
        print("Sub1 class disp2")

class Sub2(Sub1):
    def disp3(self):
        print("Sub2 class disp3")

s2 = Sub2()
s2.disp1()
s2.disp2()
s2.disp3()