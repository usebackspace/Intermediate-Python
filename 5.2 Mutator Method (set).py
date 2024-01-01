class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def set_make(self,brand):
        self.make = brand 

    def set_model(self,mod):
        self.model = mod
    

c= Car('Ford','Mustang')
print(c.make)
print(c.model)

c.make='Lamborghini'
c.model='Avantador'

print(f'New Company in the market is {c.make}')
print(f'Model launch is {c.model}')
