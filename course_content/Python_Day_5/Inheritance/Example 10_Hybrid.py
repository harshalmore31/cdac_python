# Hybrid inheritance

class GP:
    def disp1(self):
        print("GP disp1")


class Parent1(GP):
    def disp2(self):
        print("Parent1 disp2")


class Parent2(GP):
    def disp3(self):
        print("Parent2 disp3")

class Child(Parent1,Parent2):
    def disp4(self):
        print("Child disp4")

c = Child();
c.disp1()  # no problem here
'''
In some languages, because of how inheritance is implemented, when you call "c.disp1()", 
it is ambiguous whether you actually want the overridden "disp1()" from Parent1, or the one from Parent2.

Python doesn't have this problem because of the Method Resolution Order (MRO). 
Briefly, when you inherit from multiple classes, if their method names conflict, the first one named takes precedence. 
Since we have specified Child(Parent1,Parent2), Parent1.disp1 is called before Parent2.disp1.
'''
c.disp2()
c.disp3()
c.disp4()