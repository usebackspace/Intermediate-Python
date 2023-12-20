class Vehicle:                      # Parent class or Base Class or Super Classs
    speed = 0
    
    def __init__(self):                             # Without Argument
        print('Which car do you have to race ?')

    # def __init__(self,car):                       # with Argument
    #     self.car = car
    #     print('Which car do you have to race ?')
    #     print(f'I have {self.car}')

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
        print(f'Press Start Button to start the car')               # Without Argument
        # print(f'Press Start Button to start {self.car}')         # with Argument


    def honk(self):
        print(f"Press honk button to honks loudly.")

# Creating an instance of the Car class
jaquar = Car()                   # Without Argument
# jaquar = Car('Ford GT-40')     # With Argument

# Accessing methods
jaquar.start_engine()
# jaquar.honk()
# jaquar.car_info()
# jaquar.accelerate(50)
# jaquar.rtr()
