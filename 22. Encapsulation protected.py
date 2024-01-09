class Vehicle:
    def __init__(self, color, wheels):
        self._color = color
        self._wheels = wheels

class Car(Vehicle):
    def __init__(self, color, wheels, doors):
        super().__init__(color, wheels)
        self._doors = doors

    def car_detail(self):
        print(f'Color of Car {self._color}, No. of Wheel {self._wheels}, No. of door {self._doors}')

# Creating objects and using methods
car = Car("red", 4, 4)
car.car_detail()  # Specific to Car

# Accessing protected variable using object
print('Before changing protected variable of wheel:',car._wheels)
car._wheels=10         # Modifying protected value
print('After changing protected variable of wheel:',car._wheels)

print('Number of cars door',car._doors)