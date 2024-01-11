class Parent:                                # Parent class or Base Class or Super Class
    
    def parent_property(self):
        print('parent''s property')

class Brother(Parent):                          # Child class or Derived class or Sub Class
    
    def brother_property(self):
        print('Child''s property')

class Sister(Parent):                          # Child class or Derived class or Sub Class
    
    def sister_property(self):
        print('GrandChild''s property')

# Creating an instance of the Brother class (Child Class)
b = Brother()     
b.brother_property()
# b.sister_property()     # Brother cannot access sister property and vise versa
b.parent_property()

# Creating an instance of the Sister class (Child Class)
s=Sister()
s.sister_property()
# s.brother_property()  
s.parent_property()


# Creating an instance of the parent class (Parent Class)
p=Parent()
p.parent_property()
# p.brother_property()    # Parent class cannot access child property

print()

#========================================================================================================

class Vehicle:
    def __init__(self, color):
        self.color = color

    def info(self):
        print("Vehicle Info.")

class Car(Vehicle):
    def __init__(self, color, doors):
        super().__init__(color)
        self.doors = doors

    def car_detail(self):
        print(f'Color of Car {self.color}, No. of door {self.doors}')

class Truck(Vehicle):
    def __init__(self, color, cargo):
        super().__init__(color)
        self.cargo = cargo

    def truck_detail(self):
        print(f'Color of Car {self.color}, Cargo Capacity {self.cargo}')

# Creating objects and using methods
car = Car("red", 4)
car.info()  # Inherited from Vehicle
car.car_detail()  # Specific to Car

print()

truck = Truck("blue", 1000)
truck.info()  # Inherited from Vehicle
truck.truck_detail()  # Specific to Truck
