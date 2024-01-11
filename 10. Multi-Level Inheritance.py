class Parent:                                # Parent class or Base Class or Super Class

    def parent_property(self):
        print('parent''s property')

class Child(Parent):                          # Child class or Derived class or Sub Class
    
    def child_property(self):
        print('Child''s property')

class GrandChild(Child):                         

    def grandchild_property(self):
        print('GrandChild''s property')

# Creating an instance of the GrandChild class (Child Class)
gc = GrandChild()     
gc.grandchild_property()
gc.child_property()
gc.parent_property()

# Creating an instance of the Child class (Child Class)
c=Child()
c.child_property()
# c.grandchild_property()

# Creating an instance of the parent class (Parent Class)
parent=Parent()
parent.parent_property()
# parent.child_property()    # Parent class cannot access child class method

print()

#========================================================================================================
# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def vehicle(self):
        print(f"Vehicle: {self.brand}")

# Child class inheriting from parent class- Vehicle
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)      # Calling the constructor base class vehicle (parent class - Vehicle)
        self.num_doors = num_doors

    def car(self):
        print(f"Doors: {self.num_doors}")

# Grand Child inheriting from child class - Car
class SportsCar(Car):
    def __init__(self, brand, num_doors, top_speed):
        super().__init__(brand, num_doors) # Calling the constructor of the immediate base class i.e (child class -Car)
        self.top_speed = top_speed

    def sportscar(self):
        print(f"Top Speed: {self.top_speed} kph")

# Create an instance of SportsCar
sports_car = SportsCar(brand="McLaren", num_doors=2, top_speed=350)

# Accessing sportscar method
sports_car.sportscar()

# Accessing car method through Grand Child class (sportscar)
sports_car.car()

# Accessing vehicle method through Grand Child class (sportscar)
sports_car.car()

#===================================================================================================

# Same Inheritance concept apply here also :
# 1. Grand child can access members of child class and parent class.
# 2. Child class can access members of parent class but cannot access members of grand child class
# 3. Parent class can neither access members of Child class nor Grand child class