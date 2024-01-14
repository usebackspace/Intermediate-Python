class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_sound(animal):
    return animal.speak()

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Calling the function with different objects
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!
print(make_sound(duck))  # Output: Quack!
