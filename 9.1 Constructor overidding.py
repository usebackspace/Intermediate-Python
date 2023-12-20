class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel
        print(f"Speed: {self.speed}, Fuel: {self.fuel}")

    def display_info(self):
        print(f"Speed: {self.speed}, Fuel: {self.fuel}")

class Car(Vehicle):
    def __init__(self, speed, fuel, brand, model):
        # Call the constructor of the parent class
        super().__init__(speed, fuel)
        self.brand = brand
        self.model = model
        print(f"Brand: {self.brand}, Model: {self.model}")


    def display_info(self):
        # Call the display_info method of the parent class
        super().display_info()
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating an instance of the Car class
toyota = Car(speed=60, fuel='Gasoline', brand='Toyota', model='Camry')

# Accessing attributes from both Vehicle and Car classes
# print(f"Speed: {toyota.speed}, Fuel: {toyota.fuel}, Brand: {toyota.brand}, Model: {toyota.model}")

# Calling the display_info method of the Car class
# toyota.display_info()
