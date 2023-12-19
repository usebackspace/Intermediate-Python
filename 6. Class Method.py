class Car:
    speed = 0

    def __init__(self, make, model, year):
        self.make = make        # Instance variable
        self.model = model
        self.year = year
        

    def accelerate(self, speed_increase):  # Instance Method
        self.speed += speed_increase


    def display_speed(self):
        print(f"The current speed of the {self.year} {self.make} {self.model} is {self.speed} mph.")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)
my_car1 = Car(make="Toyota", model="Camry", year=2022)

# Using instance methods to interact with the car
my_car.display_speed()
my_car.accelerate(20)
print(my_car.speed)

print()

print(my_car1.speed)

print('----- Using Class Method -----')

class Car:
    speed = 0
    def __init__(self, make, model, year):
        self.make = make        # Instance variable
        self.model = model
        self.year = year

    @classmethod
    def accelerate(cls, speed_increase):  # Instance Method
        cls.speed += speed_increase
        # print(cls.speed)
        #print(self.speed)           # 3 P of D



    def display_speed(self):
        print(f"The current speed of the {self.year} {self.make} {self.model} is {self.speed} mph.")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)
my_car1 = Car(make="Ford", model="Mustang", year=2022)

# Using instance methods to interact with the car
my_car.display_speed()
my_car.accelerate(20)

print(my_car.speed)

print('--- After Updating ----')
my_car.display_speed()

print(my_car1.speed)


