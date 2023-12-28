print('---- Method Overloading in Java------')

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Usage
calc = Calculator()
result1 = calc.add(2, 3)       # Calls the first add method
result2 = calc.add(2, 3, 4)    # Calls the second add method


#=========================================================================================================

print('---- Method Overloading in Python------')
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Usage
calc = Calculator()
result1 = calc.add(2, 3)       # Calls the version with two parameters
result2 = calc.add(2, 3, 4)    # Calls the version with three parameters
