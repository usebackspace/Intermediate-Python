class parent:                                # Parent class or Base Class or Super Class
    def __init__(self):
        print("parent class Constructor")

    def parent_property(self):
        print('parent''s property')

class Child(parent):                          # Child class or Derived class or Sub Class
    def __init__(self):
        print('Child class Constructor')
    
    def child_property(self):
        print('Child''s property')

# Creating an instance of the Child class ( Child Class)
ch = Child()     
ch.child_property()
ch.parent_property()

# Creating an instance of the parent class ( Parent Class)
parent=parent()
parent.parent_property()
# parent.child_property()    # Parent class cannot access child class method

print()


#===========================================================================================================

class Vehicle:                      # Parent class or Base Class or Super Class

    def car_info(self):
        print(f"Jaquar F-type  2020 edititon")

    def rtr(self):
        print(f"Ready To Race ")

class Car(Vehicle):                 # Child class or Derived class or Sub Class
    
    def start_engine(self):
        print('Press Start Button to start the car')

    def honk(self):
        print(f"Press honk button to honks loudly.")

# Creating an instance of the Car class ( Child Class)
jaquar = Car()
jaquar.start_engine()
# jaquar.honk()
# jaquar.car_info()
jaquar.rtr()

# Parent Class object cannot access attributes and method child class 

# Creating an instance of the Vehicle class ( Parent Class)
veh = Vehicle()
# veh.honk()