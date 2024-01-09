class Car:
    def __init__(self, make, model, year):
        self.make = make                        # Instance Attribute of a class
        self.model = model
        self.year = year

    def start(self):                           # Instance Method of a class
        print(f"The {self.year} {self.make} {self.model} is starting.")


# Create an instance of the Car class
toyota = Car(make="Toyota", model="Camry", year=2022)

# Using methods to interact with the car
toyota.start()

print(toyota.model)  # Public variable



