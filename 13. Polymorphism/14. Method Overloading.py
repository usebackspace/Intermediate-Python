# print('---- Method Overloading in Java------')

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# # Usage
# calc = Calculator()
# result1 = calc.add(2, 3)       # Calls the first add method
# result2 = calc.add(2, 3, 4)    # Calls the second add method


#=========================================================================================================

print('---- Method Overloading in Python------')
class Calculator:
    def add(self, a, b, c=None):      #Or we can take value of c=0
        if c is not None:
            return a + b + c
        else:
            return a * b

# Usage
calc = Calculator()
result1 = calc.add(2, 3)       # Calls the version with two parameters
result2 = calc.add(2, 3, 4)    # Calls the version with three parameters

print(f'Result of two parameter is {result1}')
print(f'Result of three parameter is {result2}')

print()

#=======================================================================================================

print('----- Method Overloading Using Variable length Argument -----')
class Calculator:
    def add(self, *args):
        return sum(args)

# Create an instance of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
result1 = calc.add(1)
result2 = calc.add(1, 2)
result3 = calc.add(1, 2, 3)

print(result1)  # Output: 1
print(result2)  # Output: 3
print(result3)  # Output: 6
