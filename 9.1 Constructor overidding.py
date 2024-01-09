class Vehicle:                      # Parent class or Base Class or Super Classs
    
    def __init__(self):                           
        print('This is a vehicle class Constructor ')

    # def __init__(self,model):
    #     self.model = model                           
    #     print('Model of car is ',self.model)

    def car_info(self): 
        print(f"Jaquar F-type  2020 edititon")

    
class Car(Vehicle):                 # Child class or Derived class or Sub Class
    
    def __init__(self):
        super().__init__()
        print('This is Car class Constructor')
    
    # def __init__(self,model,price):
    #     self.price =price
    #     super().__init__(model)
    #     print('This is Car class Constructor')
    #     print('Model of car is ',self.model)
    #     print('Price of car is ',self.price)

    def start_engine(self):
        print(f'Press Start Button to start the car')              
        

# Creating an instance of the Car class
jaquar = Car()                
        
# jaquar = Car('Ford',6000000)                

# Accessing methods
jaquar.start_engine()
# jaquar.honk()
# jaquar.car_info()


# When we pass parameter to the instance of parent class we have to pass parameter through child class constructor