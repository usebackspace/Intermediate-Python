class Parent:  
                                  # Parent class or Base Class or Super Class
    def parent_property(self):
        print('parent''s property')

class Child(Parent):                          # Child class or Derived class or Sub Class
    
    def child_property(self):
        print('Child''s property')

# Creating an instance of the Child class ( Child Class)
ch = Child()     
ch.child_property()
ch.parent_property()

print()

# Creating an instance of the parent class ( Parent Class)
par=Parent()
par.Parent_property()
# parent.child_property()    # Parent class cannot access child class method

print()


#===========================================================================================================

class Vehicle:                      # Parent class or Base Class or Super Class

    def car_info(self):
        print(f"Jaquar F-type  2020 edititon")


class Car(Vehicle):                 # Child class or Derived class or Sub Class
    
    def start_engine(self):
        print('Press Start Button to start the car')


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