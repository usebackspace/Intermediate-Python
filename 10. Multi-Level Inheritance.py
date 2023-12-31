class Parent:                                # Parent class or Base Class or Super Class
    def __init__(self):
        print("parent class Constructor")

    def parent_property(self):
        print('parent''s property')

class Child(Parent):                          # Child class or Derived class or Sub Class
    def __init__(self):
        super().__init__()
        print('Child class Constructor')
    
    def child_property(self):
        print('Child''s property')

class GrandChild(Child):                         
    def __init__(self):
        super().__init__()
        print('GrandChild class Constructor')
    
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
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

    def vehicle(self):
        print(' This is a vehicle class constructor')

# Child class inheriting from parent class- Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)      # Calling the constructor base class vehicle (parent class - Vehicle)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()        # Call the display_info method of the base class (parent class - Vehicle)
        print(f"Doors: {self.num_doors}")

    def car(self):
        print(' This is a car class constructor')

# Grand Child inheriting from child class - Car
class SportsCar(Car):
    def __init__(self, brand, model, num_doors, top_speed):
        super().__init__(brand, model, num_doors) # Calling the constructor of the immediate base class i.e (child class -Car)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()  #Calling the constructor of the immediate base class i.e (child class -Car)
        print(f"Top Speed: {self.top_speed} kph")

    def sportscar(self):
        print(' This is a sports car class constructor')

# Create an instance of SportsCar
sports_car = SportsCar(brand="McLaren", model="P1", num_doors=2, top_speed=350)

sports_car.display_info()

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