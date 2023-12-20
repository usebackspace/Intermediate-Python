class Vehicle:                      # Parent class or Base Class or Super Classs
    speed = 0

    def car_info(self):
        print(f"Jaquar F-type  2020 edititon")

    @classmethod
    def accelerate(cls, speed_increment):
        cls.speed += speed_increment
        print(f"Current speed is: {cls.speed} km/h.")

    @staticmethod
    def rtr():
        print(f"Ready To Race ")

    
class Car(Vehicle):                 # Child class or Derived class or Sub Class
    
    def start_engine(self):
        print('Press Start Button to start the car')

    def honk(self):
        print(f"Press honk button to honks loudly.")

# Creating an instance of the Car class
jaquar = Car()

# Accessing methods
jaquar.start_engine()
# jaquar.honk()
# jaquar.car_info()
# jaquar.accelerate(50)
# jaquar.rtr()
