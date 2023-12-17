class Circle:
    pi = 3.14               # Class Variable

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius * self.radius

Circle.pi=30       # CLass Variable are access using class_name.variable_name
                   # Value of class variable is common for all object 
c1=Circle(1)
c1.radius=10
print(c1.calculate_area())

c2=Circle(1)
c2.pi=50     # Changing class variable value using object... value of pi=50 will be for this instance only   
print(c2.calculate_area())

c3=Circle(1)
print(c3.calculate_area())


