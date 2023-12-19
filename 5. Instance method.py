class Car:
    def __init__(self, make, model, year):
        self.make = make        # Instance variable
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_increase):  # Instance Method
        self.speed += speed_increase

    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
        else:
            self.speed = 0

    def display_speed(self):
        print(f"The current speed of the {self.year} {self.make} {self.model} is {self.speed} mph.")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

# Using instance methods to interact with the car
my_car.display_speed()
my_car.accelerate(20)
my_car.display_speed()
my_car.brake(10)
my_car.display_speed()
