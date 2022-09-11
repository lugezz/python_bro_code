from oop_car2 import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

# Car.wheels = 2 -> Change for all
car_1.wheels =  2 # -> Change just this instance

print(car_1.wheels)
print(car_2.wheels)