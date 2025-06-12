class Top1:
    def disp1(self):
        print("Top1 method")

class Bottom1(Top1):
    def disp1(self):
        print("Bottom1 method")

class Bottom2(Top1):
    def disp1(self):
        print("Bottom2 method")

class Bottom3(Top1):
    def disp1(self):
        print("Bottom3 method")

def perform(obj):
    obj.disp1()

perform(Bottom1())
perform(Bottom2())
perform(Bottom3())