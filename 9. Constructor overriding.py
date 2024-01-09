class Vehicle:                      # Parent class or Base Class or Super Classs
    
    def __init__(self):                           
        print('This is a vehicle class Constructor ')

    def car_info(self):
        print(f"Jaquar F-type  2020 edititon")

 
class Car(Vehicle):                 # Child class or Derived class or Sub Class
    
    # def __init__(self):
    #     print('This is Car class Constructor')

    def start_engine(self):
        print(f'Press Start Button to start the car')              
        

# Creating an instance of the Car class
jaquar = Car()                

# Accessing methods
jaquar.start_engine()
# jaquar.honk()
# jaquar.car_info()

# 1. If we define class constructor in parent class and create a Instance of child class, class constructor of 
#    PARENT class get called automatically.

# 2. If define class constructor in  both parent class and child class and create a Instance of child class,
#    class constructor of CHILD class get called automatically.

# 3. First preference will be always  child class constructor