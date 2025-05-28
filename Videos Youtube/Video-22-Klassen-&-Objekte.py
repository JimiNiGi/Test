
class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None



car1 = Car()
print(car1.car_brand)
car1.car_brand = "Audi"
car1.horse_power = "250"
car1.color = "Blau"

print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car2 = Car()
car2.car_brand = "BMW"
car2.horse_power = 210
car2.color = "Schwarz"

print(car2.car_brand)
print(car2.horse_power)
print(car2.color)


