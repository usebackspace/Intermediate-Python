
class Addition():
    def operation(self, a, b):
        result = a + b
        print(f"Addition Result: {result}")

class Multiplication(Addition):
    def operation(self, a, b):
        result = a * b
        # super().operation(300,700)
        print(f"Multiplication Result: {result}")

mul = Multiplication()

mul.operation(10,20)

print()

#========================================================================================================
# Base class
print('----- Example of Method overidding in multilevel inheritance -----')
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Vehicle: {self.brand}")

    def vehicle(self):
        print(' This is a vehicle class constructor')

# Child class inheriting from parent class- Vehicle
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)      # Calling the constructor base class vehicle (parent class - Vehicle)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()        # Call the display_info method of the base class (parent class - Vehicle)
        print(f"Doors: {self.num_doors}")

    def car(self):
        print(' This is a car class constructor')

# Grand Child inheriting from child class - Car
class SportsCar(Car):
    def __init__(self, brand, num_doors, top_speed):
        super().__init__(brand, num_doors) # Calling the constructor of the immediate base class i.e (child class -Car)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()  #Calling the constructor of the immediate base class i.e (child class -Car)
        print(f"Top Speed: {self.top_speed} kph")

    def sportscar(self):
        print(' This is a sports car class constructor')

# Create an instance of SportsCar
sports_car = SportsCar(brand="McLaren", num_doors=2, top_speed=350)

sports_car.display_info()

# Accessing sportscar method
sports_car.sportscar()

# Accessing car method through Grand Child class (sportscar)
sports_car.car()

# Accessing vehicle method through Grand Child class (sportscar)
sports_car.car()

#===================================================================================================

# Same Inheritance concept apply here also :
# 1. Grand child can access members of child class and parent class.
# 2. Child class can access members of parent class but cannot access members of grand child class
# 3. Parent class can neither access members of Child class nor Grand child class