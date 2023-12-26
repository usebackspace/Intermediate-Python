class Vehicle:
    def __init__(self, color, number_of_wheels):
        self.color = color
        self.number_of_wheels = number_of_wheels

    def info(self):
        print("Vehicle Info.")


class Car(Vehicle):
    def __init__(self, color, number_of_wheels, number_of_doors):
        super().__init__(color, number_of_wheels)
        self.number_of_doors = number_of_doors

    def car_detail(self):
        print(f'Color of Car {self.color}, No. of Wheel {self.number_of_wheels}, No. of door {self.number_of_doors}')

class Truck(Vehicle):
    def __init__(self, color, number_of_wheels, cargo_capacity):
        super().__init__(color, number_of_wheels)
        self.cargo_capacity = cargo_capacity

    def truck_detail(self):
        print(f'Color of Car {self.color}, No. of Wheel {self.number_of_wheels}, Cargo Capacity {self.cargo_capacity}')

# Creating objects and using methods
car = Car("red", 4, 4)
car.info()  # Inherited from Vehicle
car.car_detail()  # Specific to Car

print()

truck = Truck("blue", 6, 1000)
truck.info()  # Inherited from Vehicle
truck.truck_detail()  # Specific to Truck
