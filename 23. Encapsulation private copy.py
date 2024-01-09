class Car:
    def __init__(self, make, model, year):
        self.__make = make                        # Instance Attribute of a class
        self.__model = model
        self.__year = year

    def start(self):                           
        print(f"The {self.__year} {self.__make} {self.__model} is starting.")
  
    def __info(self):                           # Private Method of a class
        print(f"My car is {self.__year} {self.__make} {self.__model} .")

    def display_info(self):
        return self.__info()


# Create an instance of the Car class
toyota = Car(make="Toyota", model="Camry", year=2022)

# Using methods to interact with the car
toyota.start()

# print(toyota.__model)  # Private variable

# print(dir(toyota))
print(toyota._Car__make)    # Name mangling

# toyota.__info()

toyota._Car__info()


toyota.display_info()