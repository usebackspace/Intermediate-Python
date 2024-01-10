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

#==========================================================================================================
# Create an instance of the Car class
toyota = Car(make="Toyota", model="Camry", year=2022)

# Accessing start method having private variable
toyota.start()

# Accessing Private Method and Private Variable using Public Method
toyota.display_info()

#==========================================================================================================
# We try to access private method and private variable outside the class it will show an error

# print(toyota.__model)  # Private variable
# toyota.__info()        # Private method


#==========================================================================================================
# Accessing Private Method and Variable using Name Mangling
# print(dir(toyota))

# print(toyota._Car__make)    # Name mangling
# toyota._Car__info()

