class Car:
    def __init__(self, make, model, year):
        self.make = make                        # Instance Attribute of a class
        self.model = model
        self.year = year

    def start(self):                           # Instance Method of a class
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def display_info(self):
        print(f"\nCar Information:\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n")

# Create an instance of the Car class
toyota = Car(make="Toyota", model="Camry", year=2022)

# Using methods to interact with the car
toyota.display_info()
toyota.start()



