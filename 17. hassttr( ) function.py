class Dog:
    def speak(self):
        return "Woof!"
   
class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def run(self):
        return "Slow"

def make_sound(animal):

    print(animal.speak())

    # if hasattr(animal,'speak'):
    #     print(animal.speak())
    
    # if hasattr(animal,'run'):
    #     print(animal.run())

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Calling the function with different objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
make_sound(duck)  # Output: Quack!


