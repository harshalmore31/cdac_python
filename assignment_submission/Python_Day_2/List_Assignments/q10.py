class Car:
    def __init__(self, model, isautomatic):
        self.model = model
        self.isautomatic = isautomatic

    def get_model(self):
        return self.model

    def get_isautomatic(self):
        return self.isautomatic

car1 = Car("Swift", True)
car2 = Car("Alto", False)
car3 = Car("i20", True)
car4 = Car("Nexon", False)
car5 = Car("Baleno", True)

car_list = [car1, car2, car3, car4, car5]

automatic_cars = [car for car in car_list if car.get_isautomatic()]

print("All Cars:")
for car in car_list:
    print(f"Model: {car.get_model()}, Automatic: {car.get_isautomatic()}")

print("\nAutomatic Cars:")
for car in automatic_cars:
    print(f"Model: {car.get_model()}, Automatic: {car.get_isautomatic()}")