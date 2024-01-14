class Animal:
    def feed(self):
        pass 

class Lion(Animal):
    def feed(self):
        print("Feeding meat to the lion")

class Elephant(Animal):
    def feed(self):
        print("Feeding plants to the elephant")

class Bird(Animal):
    def feed(self):
        print("Feeding seeds to the bird")

def perform_feeding(animal):
    animal.feed()

# Usage
lion = Lion()
elephant = Elephant()
bird = Bird()

perform_feeding(lion)       #  Feeding meat to the lion
perform_feeding(elephant)   #  Feeding plants to the elephant
perform_feeding(bird)       #  Feeding seeds to the bird



