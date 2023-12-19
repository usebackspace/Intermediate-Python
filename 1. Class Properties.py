class Car:
    def __init__(zself, make, model, year, color, fuel_type, is_running=True, speed=0):
        self.make = make                        # Instance Attribute of a class
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.is_running = is_running
        self.speed = speed

    def start(self):                           # Instance Method of a class
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is starting.")
        else:
            print("Press Start Button To Start The Car.")

    def stop(self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model} is stopping.")
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
toyota = Car(make="Toyota", model="Camry", year=2022, color="Blue", fuel_type="Gasoline")

# Using methods to interact with the car
toyota.display_info()
toyota.start()
toyota.accelerate(30)
toyota.stop()

