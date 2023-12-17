class Car:
    def __init__(self, make, model, year, color, fuel_type, is_running=False, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.is_running = is_running
        self.speed = speed

    def start(self):
        if not self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is starting.")
            self.is_running = True
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is stopping.")
            self.is_running = False
            self.speed = 0
        else:
            print("The car is already stopped.")

    def accelerate(self, speed_increase):
        if self.is_running:
            self.speed += speed_increase
            print(f"The car is accelerating. Current speed: {self.speed} mph.")
        else:
            print("Start the car before accelerating.")

    def display_info(self):
        print(f"\nCar Information:\n"
              f"Make: {self.make}\n"
              f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n"
              f"Fuel Type: {self.fuel_type}\n"
              f"Is Running: {self.is_running}\n"
              f"Current Speed: {self.speed} mph\n")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022, color="Blue", fuel_type="Gasoline")

# Use methods to interact with the car
my_car.display_info()
my_car.start()
my_car.accelerate(30)
my_car.display_info()
my_car.stop()
my_car.display_info()
