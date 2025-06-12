class Vehicle:
    def start(self):
        print("Vehicle started")

class FourWheeler(Vehicle):
    def start(self):
        print("FourWheeler started") 

car = FourWheeler()
car.start()